#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" pykemon.models

This files holds all the class definitions representing resources from PokeAPI.
"""


class DateTimeObject(object):

    def __init__(self, bundle):
        self.name = bundle['name']
        self.resource_uri = bundle['resource_uri']
        self.created = bundle['created']
        self.modified = bundle['modified']


class Pokemon(DateTimeObject):
    """
    This class represents a single Pokemon resource
    """

    def __init__(self, bundle):
        super(Pokemon, self).__init__(bundle)
        self.id = bundle['national_id']
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


class Move(DateTimeObject):
    """
    This class represents a single Move resource
    """

    def __init__(self, bundle):
        super(Move, self).__init__(bundle)
        self.id = bundle['id']
        self.accuracy = bundle['accuracy']
        self.category = bundle['category']
        self.power = bundle['power']
        self.pp = bundle['pp']


class Type(DateTimeObject):
    """
    This class represents a single Type Resource
    """

    def __init__(self, bundle):
        super(Type, self).__init__(bundle)
        self.id = bundle['id']
