# Copyright (c) 2020, Intel Corporation
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of Intel Corporation nor the names of its contributors
#       may be used to endorse or promote products derived from this software
#       without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.import sys
import sys

if sys.version_info[0] < 3:
    exit('Python 3 is required')
    
import argparse
from functools import wraps
import glob
import os
import os.path
from os.path import join
import platform
import requests
import shutil
from string import Template
import stat
import string
import subprocess
import tarfile
import venv
from zipfile import ZipFile

sys.path.insert(0, os.path.abspath(join('source','conf')))
import common_conf

oneapi_spec_version = common_conf.env['oneapi_version']

sphinx_build   = 'sphinx-build'
source_dir     = 'source'
build_dir      = 'build'
doxygen_dir    = 'doxygen'
doxygen_xml    = join(doxygen_dir,'xml','index.xml')

indent = 0

def action(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        global indent
        log('%s: %s' % (args[1] if len(args) > 1 and args[1] else wrapped.__name__, args[0]))
        indent += 2
        x = func(*args, **kwargs)
        indent -= 2
        return x
    return wrapped

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        log('cd ' + self.newPath)
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def log(*args, **kwargs):
    print(indent * ' ' + ' '.join(map(str,args)), flush = True, **kwargs)
    
def shell(c):
    log(c)
    if cl_args.dry_run:
        return
    subprocess.check_call(c, shell=True)

def rm(dir):
    log('rm -rf', dir)
    if cl_args.dry_run:
        return
    shutil.rmtree(dir, ignore_errors=True)
    
from distutils.dir_util import copy_tree as copy_tree_update

def copytree(src, dst, dirs_exist_ok=False):
    log('cp -r', src, dst)
    if cl_args.dry_run:
        return
    # dirs_exist_ok needs python 3.8 or later, use copy_tree_update
    # for now
    if dirs_exist_ok:
        copy_tree_update(src, dst)
    else:
        shutil.copytree(src, dst)
    
def copy(src, dst):
    log('cp', src, dst)
    if cl_args.dry_run:
        return
    shutil.copy(src, dst)
    
def makedirs(path):
    log('mkdir -p', path)
    if cl_args.dry_run:
        return
    os.makedirs(path)

def sphinx(root, target):
    if not cl_args.verbose:
        os.environ['LATEXMKOPTS'] = '--silent'
        os.environ['LATEXOPTS'] = '-interaction=nonstopmode -halt-on-error'
    sphinx_args = '-N -j auto'
    if not cl_args.verbose:
        sphinx_args += ' -q'
    if cl_args.a:
        sphinx_args += ' -a'
    if cl_args.n:
        sphinx_args += ' -n'
    shell('%s -M %s %s %s %s' % (sphinx_build,
                                 target,
                                 join(root,source_dir),
                                 join(root,build_dir),
                                 sphinx_args))

def get_env(var):
    return os.environ[var] if var in os.environ else ''
    
def root_only(root):
    if root != '.':
        exit('Error: Only works from root')

@action
def dockerbuild(root, target=None):
    root_only(root)
    copy('requirements.txt', 'docker')
    copy('ubuntu-packages.txt', 'docker')
    copy('scripts/install.sh', 'docker')
    shell('docker build'
          ' --build-arg http_proxy=%s'
          ' --build-arg https_proxy=%s'
          ' --build-arg no_proxy=%s'
          ' --tag rscohn2/oneapi-spec docker'
          % (get_env('http_proxy'), get_env('https_proxy'), get_env('no_proxy')))

@action
def dockerpush(root, target=None):
    shell('docker push rscohn2/oneapi-spec')

@action
def dockerrun(root, target=None):
    root_only(root)
    shell('docker run --rm -it'
          ' -e http_proxy=%s'
          ' -e https_proxy=%s'
          ' -e no_proxy=%s'
          ' --user %s:%s'
          ' --volume=%s:/build'
          ' --workdir=/build'
          ' rscohn2/oneapi-spec'
          % (get_env('http_proxy'), get_env('https_proxy'), get_env('no_proxy'),
             os.getuid(), os.getgid(), os.getcwd()))

@action
def clean(root, target=None):
    apply_dirs(root, 'clean')
    sphinx(root, 'clean')

def command(root, target):
    commands[target](root, target)

def apply_dirs(root, target):
    elements = join(root,'source','elements')
    if os.path.exists(elements):
        for dir in dirs:
            command(join(elements,dir), target)

def up_to_date(target, deps):
    if not os.path.exists(target):
        return False
    for dep in deps:
        if os.path.getmtime(target) < os.path.getmtime(dep):
            return False
    return True

def doxygen_files(root):
    return [join(root,'Doxyfile')] + glob.glob(join(root,'include','**'), recursive=True)

def doxygen(root, target=None):
    with cd(root):
        doxyfile = 'Doxyfile'
        if (not os.path.exists(doxyfile) or
            up_to_date(join(root, doxygen_xml), doxygen_files(root))):
            return
        shell('doxygen %s' % doxyfile)
    
@action
def prep(root='.', target=None):
    apply_dirs(root, 'prep')
    doxygen(root)
    
@action
def build(root, target):
    prep(root)
    sphinx(root, target)

def site_zip():
    with ZipFile('site.zip', 'w') as site_zip:
        for r, dirs, files in os.walk('site', topdown=True):
            # Exclude DAL API because it is 1.7G
            if os.path.basename(r) == 'oneDAL':
                dirs = remove_elements(dirs, ['api', '_sources'])
            for file in files:
                site_zip.write(join(r, file))
    
# content served on buckets
s3_prod_root = 's3://oneapi.com/spec'
s3_pre_root = 's3://pre.oneapi.com/spec'

# served uncached
cloudfront_prod_root = 'https://d9mamou20v67v.cloudfront.net'
cloudfront_pre_root = 'https://d1c71xsfq9wxv8.cloudfront.net'

# cached by akamai
akamai_prod_root = 'https://spec.oneapi.com'
akamai_pre_root = 'https://spec.pre.oneapi.com'

pdf_name = 'oneAPI-spec.pdf'

@action
def prod_publish(root, target=None):
    # sync versions directory from pre to prod
    shell('aws s3 sync --only-show-errors --delete %s/versions/latest %s/versions/latest'
          % (s3_pre_root, s3_prod_root))
    shell('aws s3 sync --only-show-errors --delete %s/versions/latest %s/versions/%s'
          % (s3_prod_root, s3_prod_root, oneapi_spec_version))
    log('published at %s and %s'
        % (akamai_prod_root, cloudfront_prod_root))
    
def pre_publish_version(version):
    # publish html and pdf of build to pre
    html = join('build','html')
    pdf = join('build','latex',pdf_name)
    shell('aws s3 sync --only-show-errors --delete %s %s/%s'
          % (html, s3_pre_root, version))
    shell('aws s3 cp %s %s/%s/%s'
          % (pdf, s3_pre_root, version, pdf_name))

@action
def ci_publish(root, target=None):
    root_only(root)
    path = 'ci/main'
    pre_publish_version(path)
    log('published %s/%s/index.html and %s/%s/%s'
        % (cloudfront_pre_root, path, cloudfront_pre_root, path, pdf_name))
        

@action
def pre_publish(root, target=None):
    root_only(root)
    pre_publish_version('versions/%s' % oneapi_spec_version)
    shell('aws s3 sync --only-show-errors --delete %s/versions/%s %s/versions/latest'
          % (s3_pre_root, oneapi_spec_version, s3_pre_root))
    log('published %s/versions/latest/index.html and %s/versions/latest/%s'
        % (cloudfront_pre_root, cloudfront_pre_root, pdf_name))

    
@action
def spec_venv(root, target=None):
    root_only(root)
    venv.create('spec-venv', with_pip=True, clear=True)
    pip = 'spec-venv\Scripts\pip' if platform.system() == 'Windows' else 'spec-venv/bin/pip'
    shell('%s install --quiet -r requirements.txt' % pip)
    

def remove_elements(l, elements):
    for e in elements:
        if e in l:
            l.remove(e)
    return l

@action
def sort_words(root, target=None):
    with open(join('source', 'spelling_wordlist.txt')) as fin:
        lines = fin.readlines()
    with open(join('source', 'spelling_wordlist.txt'), 'w') as fout:
        for l in sorted(list(set(lines))):
            fout.write(l)
        
commands = {'clean': clean,
            'dockerbuild': dockerbuild,
            'dockerpush': dockerpush,
            'dockerrun': dockerrun,
            'html': build,
            'latexpdf': build,
            'spelling': build,
            'prep': prep,
            'pre-publish': pre_publish,
            'prod-publish': prod_publish,
            'ci-publish': ci_publish,
            'sort-words': sort_words,
            'spec-venv': spec_venv}
    
dirs = ['oneCCL',
        'oneDAL',
        'oneMKL',
        'oneTBB',
        'oneVPL',
        'dpcpp',
        'l0',
        'oneDPL',
        'oneDNN']

def main():
    global cl_args
    parser = argparse.ArgumentParser(description='Build oneapi spec.')
    parser.add_argument('action',choices=commands.keys(), default='html', nargs='?')
    parser.add_argument('root', nargs='?', default='.')
    parser.add_argument('--branch')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('-a', action='store_true', help='sphinx -a (build all files)')
    parser.add_argument('-n', action='store_true', help='sphinx -n (nitpicky mode)')
    cl_args = parser.parse_args()

    commands[cl_args.action](cl_args.root, cl_args.action)

main()
