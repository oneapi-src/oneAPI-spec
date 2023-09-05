# SPDX-FileCopyrightText: 2019-2020 Intel Corporation
#
# SPDX-License-Identifier: MIT

# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from os.path import join

repo_root = '..'
exec(open(join(repo_root, 'source', 'conf', 'common_conf.py')).read())

extensions += ['notfound.extension']  # noqa: F821

# -- Project information -----------------------------------------------------

project = u'oneAPI Specification'
copyright = u'2022, Intel Corporation'

# The short X.Y version
version = env['oneapi_version']  # noqa: F821
# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    'elements/oneART/source/versions.rst',
    'elements/oneART/source/index.rst',
    'elements/oneTBB/source/index.rst',
    'elements/oneTBB/source/uncategorized.rst',
    'elements/oneTBB/source/uncategorized/**',
    'elements/oneTBB/source/low_level_task_api.rst',
    'elements/oneTBB/source/low_level_tasking/**',
    '**/*.inc.rst',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'repository_url': 'https://github.com/oneapi-src/oneapi-spec',
    'path_to_docs': 'source',
    'use_issues_button': True,
    'use_edit_page_button': True,
    'repository_branch': 'main',
    'search_bar_text': 'Search the spec...',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_logo = '_static/oneAPI-rgb-rev-100.png'
html_favicon = '_static/favicons.png'
latex_logo = '_static/oneAPI-rgb-3000.png'

# Causing long page loads because it loads utag.js, which times out
html_js_files = ['custom.js']

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'oneAPI-spec'


# -- Options for LaTeX output ------------------------------------------------


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        'oneAPI-spec.tex',
        u'oneAPI Specification',
        u'Intel',
        'manual',
    ),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

breathe_projects = {
    "oneCCL": "elements/oneCCL/doxygen/xml",
    "oneDNN": "elements/oneDNN/doxygen/xml",
    "oneVPL": "elements/oneVPL/doxygen/xml",
}
breathe_default_project = 'oneAPI'

notfound_default_language = 'versions'

# oneDAL project directory is needed for `dalapi` extension
onedal_relative_doxyfile_dir = 'elements/oneDAL'
onedal_relative_sources_dir = 'elements/oneDAL'
onedal_enable_listing = True
