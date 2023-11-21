#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from setuptools import setup

wd = path.abspath(path.dirname(__file__))
with open(path.join(wd, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    description='Abacus',
    name='abacus',
    version='0.0.1',
    author='Bogdan Dolia',
    author_email='cr.co.erph@gmail.com',
    license='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['abacus']
)
