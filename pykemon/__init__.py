#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Paul Hallett'
__email__ = 'hello@phalt.co'
__version__ = '0.0.1'
__copyright__ = 'Copyright Paul Hallett 2013'
__license__ = 'BSD'

from api import get


"""

========
Pykemon
========

A Python wrapper for PokeAPI (http://pokeapi.co)

Usage:

>>> import pykemon
>>> pykemon.get(pokemon='bulbasaur')
<Pokemon - Bulbasaur>
>>> pykemon.get(pokemon_id=151)
<Pokemon - Mew>

"""
