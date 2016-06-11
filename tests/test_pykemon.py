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

import responses


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

    def get_client(self):
        return pykemon.V1Client()

    @responses.activate
    def test_v1_move_resource(self):
        responses.add(responses.GET, 'http://pokeapi.co/api/v1/move/1/',
                      body='''
                        {"id": 1, "name": "move"}''',
                      status=200,
                      content_type='application/json')

        client = self.get_client()
        response = client.get_move(uid=1)[0]
        assert response.name == 'move'

    @responses.activate
    def test_v1_pokemon_resource(self):
        responses.add(responses.GET, 'http://pokeapi.co/api/v1/pokemon/1/',
                      body='''
                        {"id": 1, "name": "pokemon"}''',
                      status=200,
                      content_type='application/json')

        client = self.get_client()
        response = client.get_pokemon(uid=1)[0]
        assert response.name == 'pokemon'

    @responses.activate
    def test_v1_type_resource(self):
        responses.add(responses.GET, 'http://pokeapi.co/api/v1/type/1/',
                      body='''
                        {"id": 1, "name": "types"}''',
                      status=200,
                      content_type='application/json')

        client = self.get_client()
        response = client.get_type(uid=1)[0]
        assert response.name == 'types'

    @responses.activate
    def test_v1_ability_resource(self):
        responses.add(responses.GET, 'http://pokeapi.co/api/v1/ability/1/',
                      body='''
                        {"id": 1, "name": "abilities"}''',
                      status=200,
                      content_type='application/json')

        client = self.get_client()
        response = client.get_ability(uid=1)[0]
        assert response.name == 'abilities'

    @responses.activate
    def test_v1_egg_resource(self):
        responses.add(responses.GET, 'http://pokeapi.co/api/v1/egg/1/',
                      body='''
                        {"id": 1, "name": "eggz"}''',
                      status=200,
                      content_type='application/json')

        client = self.get_client()
        response = client.get_egg(uid=1)[0]
        assert response.name == 'eggz'

    @responses.activate
    def test_v1_description_resource(self):
        responses.add(responses.GET, 'http://pokeapi.co/api/v1/description/1/',
                      body='''
                        {"id": 1, "name": "description"}''',
                      status=200,
                      content_type='application/json')

        client = self.get_client()
        response = client.get_description(uid=1)[0]
        assert response.name == 'description'

    @responses.activate
    def test_v1_sprite_resource(self):
        responses.add(responses.GET, 'http://pokeapi.co/api/v1/sprite/1/',
                      body='''
                        {"id": 1, "name": "spritez"}''',
                      status=200,
                      content_type='application/json')

        client = self.get_client()
        response = client.get_sprite(uid=1)[0]
        assert response.name == 'spritez'

    @responses.activate
    def test_v1_game_resource(self):
        responses.add(responses.GET, 'http://pokeapi.co/api/v1/game/1/',
                      body='''
                        {"id": 1, "name": "gamez"}''',
                      status=200,
                      content_type='application/json')

        client = self.get_client()
        response = client.get_game(uid=1)[0]
        assert response.name == 'gamez'


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
