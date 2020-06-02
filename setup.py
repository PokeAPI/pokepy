#!/usr/bin/env python
# coding: utf-8

import pokepy


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md', encoding='utf-8') as readme_md,\
        open('docs/history.md', encoding='utf-8') as history_md,\
        open('requirements.txt', encoding='utf-8') as requirements_txt:
    readme = readme_md.read()
    history = history_md.read()
    requirements = [req[:req.find('#')].rstrip() for req in requirements_txt.readlines()]

setup(
    name='pokepy',
    version=pokepy.__version__,
    description='A Python wrapper for PokéAPI (https://pokeapi.co)',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    license=pokepy.__license__,
    author=pokepy.__author__,
    author_email=pokepy.__email__,
    url='https://github.com/PokeAPI/pokepy',
    project_urls={'Documentation': 'https://pokeapi.github.io/pokepy/'},
    packages=['pokepy', 'pokepy.fcache'],
    package_dir={'pokepy': 'pokepy'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='pokepy PokéAPI',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    test_suite='tests',
    tests_require=['requests-mock==1.5.*'],
)
