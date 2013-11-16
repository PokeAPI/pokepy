#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" pykemon.request

This is the request factory for pykemon
All API calls made to the PokeAPI website go from here.
"""

BASE_URI = 'http://pokeapi.co/api/v1/'

CHOICES = ['pokedex', 'pokedex_id', 'pokemon', 'pokemon_id', 'move', 'move_id',
           'ability', 'ability_id', 'type', 'type_id', 'egg',
           'egg_id', 'description', 'description_id', 'sprite',
           'sprite_id', 'game', 'game_id']

import requests
import simplejson
from simplejson import JSONDecodeError
from models import (
    Pokedex, Pokemon, Move, Ability, Type, EggGroup, Description, Sprite,
    Game
)

CLASSES = {
    'pokedex': Pokedex,
    'pokemon': Pokemon,
    'move': Move,
    'egg': EggGroup,
    'description': Description,
    'sprite': Sprite,
    'game': Game
}


def _request(self, uri):
    """
    Just a wrapper around the request.get() function
    """

    r = requests.get(uri)

    if r.status_code == 200:
        return _to_json(r.text)
    else:
        return r.status_code


def _to_json(self, data):
    try:
        content = simplejson.loads(data)
        return content
    except JSONDecodeError:
        raise JSONDecodeError


def _compose(self, choice):
    """
    Figure out exactly what resource we're requesting and return the correct
    class.
    """
    choice = choice.keys()[0]
    id = choice.values()[0]

    if '_id' in choice:
        choice = choice[:-3]
    return ('/'.join([BASE_URI, choice, id, '']), choice)


def make_request(self, choice):
    """
    The entry point from pykemon.api.
    Call _request and _compose to figure out the resource / class
    and return the correct constructed object
    """
    uri, choice = _compose(choice)
    data = _request(uri)

    if type(data) == type(dict):
        resource = CLASSES[choice]
        return resource(data)
    else:
        raise ValueError('API response %s received' % data)
