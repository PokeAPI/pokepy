#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='pokepy',
    version='0.4.0',
    description='A Python wrapper for PokeAPI',
    long_description=readme + '\n\n' + history,
    author='Paul Hallett',
    author_email='hello@phalt.co',
    url='https://github.com/pokeapi/pokepy',
    packages=[
        'pokepy',
    ],
    package_dir={'pokepy': 'pokepy'},
    include_package_data=True,
    install_requires=["beckett==0.8.0"],
    license="BSD",
    zip_safe=False,
    keywords='pokepy',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
)
