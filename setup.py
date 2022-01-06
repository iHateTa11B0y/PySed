#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    packages = find_packages('src'),  # 包含所有src中的包
    package_dir = {'':'src'},   # 告诉distutils包都在src下

    name='pysed',
    version='0.1',
    author='aermi',

    entry_points = {
        'console_scripts': [
            'pt = pt:entry',
        ],
    } 
)

