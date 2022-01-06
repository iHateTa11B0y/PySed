#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re


HELP_INFO = """
Usage:
$ pt "<pythonic cmd>"

First you should know some predefined text-level.
1. _t:  text-level, `_t` refering the whole input text in your commands
2. _l:  line-level, `_l` refering the input lines<List> in your commands
3. _c: column-level `_c` refering the colums for each line <List<List>> in your commands
text-level is exclusive, which mean you can only determine one
text-level to perform pythonic commands at a time
"""


class TextLevel(object):
    def __init__(self, string):
        self._s = string

    def __call__(self, cmd):
        _t = self._s
        x = eval(cmd)
        return x

class LineLevel(object):
    def __init__(self, string):
        self._s = string
        self._lines = [_ for _ in self._s.split('\n')]

    def __call__(self, cmd):
        _l = self._lines
        try:
            x = eval(cmd)
        except Exception as e:
            print('Error, invalid command')
            exit()
        return '\n'.join(x)

class ColumnLevel(object):
    def __init__(self, string):
        self._s = string.strip()
        _cols = [_ for _ in self._s.split('\n')]
        _cols = [_.strip().split() for _ in _cols]
        self._cols = _cols

    def __call__(self, cmd):
        res = []
        for _c in self._cols:
            try:
                x = eval(cmd)
                if isinstance(x, list):
                    res.append(x)
                else:
                    res.append([x])
            except Exception as e:
                print('Error, invalid command')
                exit()
        return format_cols(res)


def format_cols(cols, align=False):
    if len(cols) == 0:
        return '\n'
    if align:
        max_len = [max([0 if idx >= len(c) else len(c[idx]) for c in cols]) for idx in range(len(cols[0]))]
        format_temp = '\t'.join([f'{{:{li}s}}' for li in max_len])
        cols = [format_temp.format(*c) for c in cols]
    else:
        cols = ['\t'.join(c) for c in cols]
    return '\n'.join(cols) 


def eval_cmd(cmds, file=None):

    if file is None:
        ss = read_from_stdin()
    else:
        ss = read_from_file(file)

    for cmd in cmds.strip(';').split(';'):
        if '_t' in cmd:
            lv = TextLevel(ss)
        elif '_l' in cmd:
            lv = LineLevel(ss)
        elif '_c' in cmd:
            lv = ColumnLevel(ss)
        else:
            print('Undetermined text-level..')
            exit()

        ss = lv(cmd) + '\n'
    sys.stdout.write(ss)

def read_from_stdin():
    text = sys.stdin.read()
    return text


def read_from_file(fn):
    if os.path.isfile(fn):
        return open(fn, 'r').readlines()
    else:
        print('Invalid File: {}'.format(fn))

