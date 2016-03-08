#!/usr/bin/env python

import os
from distutils.core import setup
from sys import maxsize
from shutil import copyfile

# Determines which is the appropriate executable for 32-bit
if maxsize == 2147483647:
    copyfile("xflux32", "xflux")
# ... or 64-bit processors
elif maxsize == 9223372036854775807:
    copyfile("xflux64", "xflux")

# Set execution permission
os.chmod("xflux", 0755)

setup(name = "f.lux indicator applet",
    version = "1.1.8",
    description = "f.lux indicator applet - better lighting for your computer",
    author = "Kilian Valkhof, Michael and Lorna Herf, Josh Winters",
    author_email = "kilian@kilianvalkhof.com",
    url = "http://www.stereopsis.com/flux/",
    license = "MIT license",
    package_dir = {'fluxgui' : 'src/fluxgui'},
    packages = ["fluxgui",],
    package_data = {"fluxgui" : ["*.glade"] },
    data_files=[('share/icons/hicolor/scalable/apps', ['fluxgui.svg', 'fluxgui-light.svg', 'fluxgui-dark.svg']),
            ('share/applications', ['desktop/fluxgui.desktop']),
            ('bin', ['xflux']),],
    scripts = ["fluxgui"],
    long_description = """f.lux indicator applet is an indicator applet to
    control xflux, an application that makes the color of your computer's
    display adapt to the time of day, warm at nights and like sunlight during
    the day""",
  )

