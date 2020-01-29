import argparse
import glob
import os
import os.path
from os.path import join
import shutil
from string import Template
import stat
import string
import subprocess
import sys
import tarfile
import venv

from git import Repo

from element import shell,sphinx
import element

sys.path.insert(0, os.path.abspath(join('source','conf')))
import common_conf

branch_name = Repo('.').active_branch.name

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        print('pushd ' + self.newPath)
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        print('popd')
        os.chdir(self.savedPath)
        
def clean(target='clean'):
    print(target)
    apply_dirs('clean')
    sphinx('clean')

def apply_dirs(target):
    for dir in dirs:
        with cd(join('source','elements',dir)):
            element.command(target)

def prep(target='prep'):
    print(target)
    apply_dirs('prep')
    
def build(target):
    print(target)
    prep()
    sphinx(target)

def ci_publish(target='ci-publish'):
    print(target)
    shell('aws s3 sync --only-show-errors --delete site s3://%s/branches/%s' % (staging_host, branch_name))
    
def prod_publish(target='prod-publish'):
    print(target)
    shell('aws s3 sync --only-show-errors --delete s3://%s/versions/%s s3://spec.oneapi.com/versions/%s'
          % (staging_host,common_conf.oneapi_spec_version, common_conf.oneapi_spec_version))
    shell('aws s3 cp s3://%s/index.html s3://spec.oneapi.com/index.html'
          % (staging_host))
    
def stage_publish(target='stage-publish'):
    print(target)
    shell('aws s3 sync --only-show-errors --delete site s3://%s/versions/%s' % (staging_host,common_conf.oneapi_spec_version))
    shell('aws s3 cp site/redirect.html s3://%s/index.html' % staging_host)
    
def spec_venv(target='spec-venv'):
    print(target)
    venv.create('spec-venv', with_pip=True, clear=True)
    shell('. spec-venv/bin/activate && pip install -r requirements.txt')
    
def clones(target='clones'):
    print(target)
    for repo_base in repos:
        dir = join('repos',repo_base)
        if os.path.exists(dir):
            continue
        uri = ('https://gitlab.devtools.intel.com/DeveloperProducts/'
               'Analyzers/Toolkits/oneAPISpecifications/%s.git' % repo_base)
        print('clone:', uri)
        Repo.clone_from(uri, dir, multi_options=['--depth','1'])
    
def redirect(target='redirect'):
    print(target)
    with open(join('source','redirect.tpl')) as fin:
        with open(join('site','redirect.html'), 'w') as fout:
            for line in fin.readlines():
                fout.write(Template(line).substitute(version=common_conf.oneapi_spec_version))
            
def site(target='site'):
    print(target)
    prep()
    sphinx('html')
    sphinx('latexpdf')
    element.rm('site')
    print('copying generated files')
    shutil.copytree(join('build','html'),'site')
    shutil.copy('build/latex/oneAPI-spec.pdf', 'site')
    redirect()
    for t in tarballs:
        tf = join('repos','oneapi-spec-tarballs','tarballs','%s.tgz' % t)
        print('untar:',tf)
        with tarfile.open(tf) as tar:
            tar.extractall('site')

def ci(target='ci'):
    print(target)
    clones()
    site()
    if branch_name == 'publish':
        stage_publish()
    else:
        ci_publish()
    
staging_host = 'staging.spec.oneapi.com'

commands = {'ci': ci,
            'ci-publish': ci_publish,
            'clean': clean,
            'clones': clones,
            'html': build,
            'latexpdf': build,
            'prep': prep,
            'prod-publish': prod_publish,
            'redirect': redirect,
            'site': site,
            'spec-venv': spec_venv,
            'stage-publish': stage_publish}
    
dirs = ['oneCCL',
        'oneDAL',
        'oneMKL',
        'oneTBB',
        'oneVPL',
        'dpcpp',
        'oneDPL',
        'oneDNN']

tarballs = ['oneMKL',
            'oneDAL']

repos = ['onetbb-spec',
         'oneapi-spec-tarballs']


def main():
    parser = argparse.ArgumentParser(description='Build oneapi spec.')
    parser.add_argument('action',choices=commands.keys())
    args = parser.parse_args()

    commands[args.action](args.action)

main()
