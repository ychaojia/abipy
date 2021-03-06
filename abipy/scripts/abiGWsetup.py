#!/usr/bin/env python
# coding: utf-8
"""
Script to write GW Input for VASP and ABINIT / set up work flows.
"""
from __future__ import unicode_literals, division, print_function

__author__ = "Michiel van Setten"
__copyright__ = " "
__version__ = "0.9"
__maintainer__ = "Michiel van Setten"
__email__ = "mjvansetten@gmail.com"
__date__ = "May 2014"

import os
import os.path

from abipy.gw.datastructures import get_spec

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    counter = 0
    #load_ps()
    spec_in = get_spec('GW')
    try:
        spec_in.read_from_file('spec.in')
    except (IOError, OSError):
        try:
            spec_in.read_from_file('$HOME/.abinit/abipy/spec.in')
        except (IOError, OSError):
            pass
        pass
    spec_in.update_interactive()
    spec_in.test()
    spec_in.write_to_file('spec.in')
    spec_in.loop_structures('i')
