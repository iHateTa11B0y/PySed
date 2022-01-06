#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from .function import *

def entry():
    if len(sys.argv) == 1:
        print(HELP_INFO)
    elif len(sys.argv) == 2:
        eval_cmd(sys.argv[1])
    else:
        eval_cmd(sys.argv[1], sys.argv[2])


