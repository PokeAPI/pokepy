#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" pykemon.models

This files holds all the class definitions representing resources from PokeAPI.
"""


class Pokemon(object):
    """
    This class represents a single Pokemon resource
    """

    def __init__(self, bundle):
        self.name = bundle['name']
        self.id = bundle['national_id']
        self.resource_uri = bundle['resource_uri']
        self.created = bundle['created']
        self.modified = bundle['modified']
        self.abilities = bundle['abilities']
        self.egg_groups = bundle['egg_groups']
        self.evolutions = bundle['evolutions']
        self.moves = bundle['moves']
        self.types = bundle['types']
        self.catch_rate = bundle['catch_rate']
        self.species = bundle['species']
        self.hp = bundle['hp']
        self.attack = bundle['attack']
        self.defense = bundle['defense']
        self.sp_atk = bundle['sp_atk']
        self.sp_def = bundle['sp_def']
        self.speed = bundle['speed']
        self.total = bundle['total']
        self.egg_cycles = bundle['egg_cycles']
        self.ev_yield = bundle['ev_yield']
        self.exp = bundle['exp']
        self.growth_rate = bundle['growth_rate']
        self.height = bundle['height']
        self.weight = bundle['weight']
        self.happiness = bundle['happiness']
        self.male_female_ratio = bundle['male_female_ratio']

    def __repr__(self):
        return '<Pokemon - %s>' % self.name.capitalize()
