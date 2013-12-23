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

    def test_name_attribute(self):
        self.assertEquals(self.poke_one.name, 'Bulbasaur')
        self.assertEquals(self.move_one.name, 'Cut')

    def test_resource_uri_attribute(self):
        self.assertEquals(self.poke_one.resource_uri, '/api/v1/pokemon/1/')
        self.assertEquals(self.move_one.resource_uri, '/api/v1/move/15/')


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
