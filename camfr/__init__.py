# Imports.

from __future__ import division

import numpy as np

import os
if not os.environ.get('NO_CAMFR_GRAPHICS'):
    from pylab import *

from _camfr import *
from camfr_PIL import *     # converted numpy* to np.*
from geometry import *      # converted numpy* to np.*
from geometry3d import *    # converted numpy* to np.*
from material import *
from section_matplotlib import *    # matplotlib functions for Section objects
from camfrversion import *

# Splash screen.

print()
print("CAMFR", camfr_version, "- Copyright (C) 1998-2007 Peter Bienstman - Ghent University.")
print()
