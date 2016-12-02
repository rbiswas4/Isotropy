from __future__ import absolute_import
import os
from .version import __VERSION__
from .mockData import *

here = __file__
basedir = os.path.split(here)[0]
example_data_dir = os.path.join(basedir, 'example_data')
