#!/usr/bin/env python
# coding: utf-8

"""
Pokepy

A Python wrapper for PokéAPI (https://pokeapi.co)

Usage:
>>> import pokepy
>>> clientV2 = pokepy.V2Client()
>>> clientV2.get_pokemon('bulbasaur')
<Pokemon - Bulbasaur>
"""

__author__ = 'Paul Hallett'
__email__ = 'hello@phalt.co'
__credits__ = ["Paul Hallett", "Owen Hallett", "Kronopt"]
__version__ = '0.6.2'
__copyright__ = 'Copyright Paul Hallett 2016'
__license__ = 'BSD'


from .api import V2Client
