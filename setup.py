#! /usr/bin/env python

# To Do:
#   Must run the following command afterwards:
#        mv /opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/camfr/_camfr.dylib  /opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/camfr/_camfr.so


from distutils.core import setup
from distutils.util import byte_compile
from distutils.command.build import build
from distutils.command.install_data import install_data

from machine_cfg import *
from camfrversion import *

# Make sure we build the libraries before running the standard build.
# Also, after the build process, strip the library of debug symbols.

class camfr_build(build):
  def run(self):

    import os
    
    #os.system("cd docs; make")
     
    os.system("scons")
    os.system(strip_command)

    return build.run(self)



# Modified install_data, changing self.install_dir to the actual library dir.
# Also byte-compiles *.py files that are outside of the regular package
# hierarchy.

class camfr_install_data(install_data):
  def run(self):

    # Byte-compile Python files.

    scripts = []
          
    #for i in self.data_files:
    #  for j in i[1]:
    #    if j[-3:] == ".py":
    #      scripts.append(j)
    #      i[1].append(j[:-3]+'.cpython-39.pyc')

    #byte_compile(scripts, verbose=1, force=True)

    # Change install dir to library dir.
    
    install_cmd = self.get_finalized_command('install')
    self.install_dir = getattr(install_cmd, 'install_lib')

    return install_data.run(self)



# Set up the module.

setup(name         = "camfr",
      version      =  camfr_version,
      description  = "CAvity Modelling FRamework",
      author       = "Peter Bienstman",
      author_email = "Peter.Bienstman@UGent.be",
      url          = "http://camfr.sourceforge.net",
      extra_path   = "camfr",
      packages     = ["examples.tutorial", "examples.other",
                      "examples.contrib", "visualisation.examples",
                      "testsuite"],
      data_files   = [(".", ["COPYRIGHT", "camfrversion.py",
                             "camfr/__init__.py",
                             "camfr/_camfr" + dllsuffix,
                             "camfr/geometry.py",
                             "camfr/geometry3d.py",
                             "camfr/material.py",
                             "camfr/RCLED.py",
                             "camfr/GARCLED.py",
                             "visualisation/camfr_PIL.py",
                             "visualisation/camfr_matlab.py",
                             "visualisation/camfr_tk.py",
                             "visualisation/slab_plot.py",
                             "visualisation/stack_plot.py",
                             "visualisation/TkPlotCanvas.py",
                             "visualisation/section_matplotlib.py",
                             "visualisation/matrix_plot_canvas.py",
                             "visualisation/gifmaker.py"])] + extra_files,
      cmdclass     = {"install_data" : camfr_install_data,
                      "build"        : camfr_build},
      )
