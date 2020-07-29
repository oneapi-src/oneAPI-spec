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
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join('..','..','..','conf')))
# element_conf needs to import this conf
sys.path.insert(0, os.path.abspath('.'))

project = 'oneVPL'

from element_conf import *

cpp_id_attributes = ['MFX_CDECL']

c_id_attributes = ['MFX_CDECL']
