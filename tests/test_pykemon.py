#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pykemon
----------------------------------

Tests for `pykemon` module.
"""

import unittest
import simplejson

import pykemon


class TestPykemon(unittest.TestCase):

    def setUp(self):
        self.poke_one = pykemon.get(pokemon='bulbasaur')
        self.move_one = pykemon.get(move_id=15)  # Cut
        self.type_one = pykemon.get(type_id=10)  # Fire
        self.ability_one = pykemon.get(ability_id=1)  # Stench
        self.egg_one = pykemon.get(egg_id=1)  # Monster
        self.description_one = pykemon.get(description_id=2)
        self.sprite_one = pykemon.get(sprite_id=152)  # Mew_auto
        self.game_one = pykemon.get(game_id=4)  # Red

    def test_name_attribute(self):
        self.assertEquals(self.poke_one.name, 'Bulbasaur')
        self.assertEquals(self.move_one.name, 'Cut')
        self.assertEquals(self.type_one.name, 'Fire')
        self.assertEquals(self.ability_one.name, 'Stench')
        self.assertEquals(self.egg_one.name, 'Monster')
        self.assertEquals(self.description_one.name, 'Bulbasaur_gen_1')
        self.assertEquals(self.sprite_one.name, 'Mew_auto')
        self.assertEquals(self.game_one.name, 'Red')

    def test_repr(self):
        self.assertEquals(str(self.poke_one), '<Pokemon - Bulbasaur>')
        self.assertEquals(str(self.move_one), '<Move - Cut>')
        self.assertEquals(str(self.type_one), '<Type - Fire>')
        self.assertEquals(str(self.ability_one), '<Ability - Stench>')
        self.assertEquals(str(self.egg_one), '<Egg - Monster>')
        self.assertEquals(
            str(self.description_one), '<Description - Bulbasaur_gen_1>')
        self.assertEquals(str(self.sprite_one), '<Sprite - Mew_auto>')
        self.assertEquals(str(self.game_one), '<Game - Red>')

    def test_resource_uri_attribute(self):
        self.assertEquals(self.poke_one.resource_uri, '/api/v1/pokemon/1/')
        self.assertEquals(self.move_one.resource_uri, '/api/v1/move/15/')
        self.assertEquals(self.type_one.resource_uri, '/api/v1/type/10/')
        self.assertEquals(self.ability_one.resource_uri, '/api/v1/ability/1/')
        self.assertEquals(self.egg_one.resource_uri, '/api/v1/egg/1/')
        self.assertEquals(
            self.description_one.resource_uri, '/api/v1/description/2/')
        self.assertEquals(self.sprite_one.resource_uri, '/api/v1/sprite/152/')
        self.assertEquals(self.game_one.resource_uri, '/api/v1/game/4/')

    def test_pokemon_complex_attribs(self):
        self.assertIn('Ivysaur', self.poke_one.evolutions)
        self.assertIn('Cut', self.poke_one.moves)
        self.assertIn('grass', self.poke_one.types)
        self.assertIn('overgrow', self.poke_one.abilities)
        self.assertIn('Monster', self.poke_one.egg_groups)
        self.assertIn('bulbasaur_gen_1', self.poke_one.descriptions)
        self.assertIn('bulbasaur', self.poke_one.sprites)

    def test_type_complex_attribs(self):
        self.assertIn('grass', self.type_one.super_effective)
        self.assertIn('water', self.type_one.weakness)
        self.assertIn('fire', self.type_one.ineffective)
        self.assertNotIn('Test', self.type_one.resistance)

    def test_egg_complex_attribs(self):
        self.assertIn('Blastoise', self.egg_one.pokemon)

    def test_description_complex_attribs(self):
        self.assertIn('red(JPN)', self.description_one.games)


class Testexceptions(unittest.TestCase):
    " Test error handling "

    def test_no_params(self):
        self.assertRaises(TypeError, pykemon.get, '')

    def test_two_params(self):
        self.assertRaises(ValueError, pykemon.get, test='test', two='two')

    def test_invalid_args(self):
        self.assertRaises(ValueError, pykemon.get, test='test')

    def test_unknown_resource(self):
        self.assertRaises(
            pykemon.exceptions.ResourceNotFoundError,
            pykemon.request._request,
            'http://pokeapi.co/api/v1/pokemon/abcdef/')

    def test_to_json_error_handling(self):
        self.assertRaises(
            simplejson.JSONDecodeError,
            pykemon.request._to_json, 'content')

    def test_make_request_error_handling(self):
        self.assertRaises(
            pykemon.exceptions.ResourceNotFoundError,
            pykemon.request.make_request,
            {'pokemon': 'Elinor'})

if __name__ == '__main__':
    unittest.main()
