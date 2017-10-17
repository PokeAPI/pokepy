#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Paul Hallett'
__email__ = 'hello@phalt.co'
__version__ = '0.2.0'
__copyright__ = 'Copyright Paul Hallett 2016'
__license__ = 'BSD'

from api import V1Client, V2Client  # NOQA


"""

========
Pykemon
========

A Python wrapper for PokeAPI (http://pokeapi.co)

Usage:

>>> import pykemon
>>> clientV1 = pykemon.V1Client()
>>> bulbasaur = clientV1.get_pokemon(uid='bulbasaur')[0]
>>> bulbasaur.name
u'Bulbasaur'
>>> mew = clientV1.get_pokemon(uid=151)[0]
>>> mew.name
u'Mew'

"""
