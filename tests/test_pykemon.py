#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pykemon
----------------------------------

Tests for `pykemon` module.
"""

# import os, sys
# sys.path.insert(0, os.path.dirname(os.getcwd()))

import unittest
import requests_mock
import pykemon


def base_test(self, resource, method="name"):
    """
    Base test function for both V1Client and V2Client

    :param self: One of the available two TestCase instances
    :param resource: Resource to be tested
    :param method: 'name' or 'id' (sometimes resources only have one)
    """
    with requests_mock.mock() as mock:
        mock.get('%s/%s/1' % (self.base_url, resource), text=self.mock_data)
        response = getattr(self.client,
                           'get_%s' % resource.replace("-", "_"))(uid=1)[0]

        if method == "name":
            self.assertEqual(response.name, 'test_name')
        elif method == "id":
            self.assertEqual(response.id, 1)


class TestV1Client(unittest.TestCase):

    def setUp(self):
        self.client = pykemon.V1Client()
        self.mock_data = '{"id": 1, "name": "test_name"}'
        self.base_url = 'https://pokeapi.co/api/v1'

    def test_pokedex_resource(self):
        base_test(self, "pokedex")

    def test_pokemon_resource(self):
        base_test(self, "pokemon")

    def test_type_resource(self):
        base_test(self, "type")

    def test_move_resource(self):
        base_test(self, "move")

    def test_ability_resource(self):
        base_test(self, "ability")

    def test_egg_resource(self):
        base_test(self, "egg")

    def test_description_resource(self):
        base_test(self, "description")

    def test_sprite_resource(self):
        base_test(self, "sprite")

    def test_game_resource(self):
        base_test(self, "game")


class TestV2Client(unittest.TestCase):

    def setUp(self):
        self.client = pykemon.V2Client()
        self.mock_data = '{"id": 1, "name": "test_name"}'
        self.base_url = 'https://pokeapi.co/api/v2'

    def test_berry_resource(self):
        base_test(self, "berry")

    def test_berry_firmness_resource(self):
        base_test(self, "berry-firmness")

    def test_berry_flavor_firmness_resource(self):
        base_test(self, "berry-flavor")

    def test_contest_type_resource(self):
        base_test(self, "contest-type")

    def test_contest_effect_resource(self):
        base_test(self, "contest-effect", "id")

    def test_super_contest_effect_resource(self):
        base_test(self, "super-contest-effect", "id")

    def test_encounter_method_resource(self):
        base_test(self, "encounter-method")

    def test_encounter_condition_resource(self):
        base_test(self, "encounter-condition")

    def test_encounter_condition_value_resource(self):
        base_test(self, "encounter-condition-value")

    def test_evolution_chain_resource(self):
        base_test(self, "evolution-chain", "id")

    def test_evolution_trigger_resource(self):
        base_test(self, "evolution-trigger")

    def test_generation_resource(self):
        base_test(self, "generation")

    def test_pokedex_resource(self):
        base_test(self, "pokedex")

    def test_version_resource(self):
        base_test(self, "version")

    def test_version_group_resource(self):
        base_test(self, "version-group")

    def test_item_resource(self):
        base_test(self, "item")

    def test_item_attribute_resource(self):
        base_test(self, "item-attribute")

    def test_item_category_resource(self):
        base_test(self, "item-category")

    def test_item_fling_effect_resource(self):
        base_test(self, "item-fling-effect")

    def test_item_pocket_resource(self):
        base_test(self, "item-pocket")

    def test_machine_resource(self):
        base_test(self, "machine", "id")

    def test_move_resource(self):
        base_test(self, "move")

    def test_move_ailment_resource(self):
        base_test(self, "move-ailment")

    def test_move_battle_style_resource(self):
        base_test(self, "move-battle-style")

    def test_move_category_resource(self):
        base_test(self, "move-category")

    def test_move_damage_class_resource(self):
        base_test(self, "move-damage-class")

    def test_move_learn_method_resource(self):
        base_test(self, "move-learn-method")

    def test_move_target_resource(self):
        base_test(self, "move-target")

    def test_location_resource(self):
        base_test(self, "location")

    def test_location_area_resource(self):
        base_test(self, "location-area")

    def test_pal_park_area_resource(self):
        base_test(self, "pal-park-area")

    def test_region_resource(self):
        base_test(self, "region")

    def test_ability_resource(self):
        base_test(self, "ability")

    def test_characteristic_resource(self):
        base_test(self, "characteristic", "id")

    def test_egg_group_resource(self):
        base_test(self, "egg-group")

    def test_gender_resource(self):
        base_test(self, "gender")

    def test_growth_rate_resource(self):
        base_test(self, "growth-rate")

    def test_nature_resource(self):
        base_test(self, "nature")

    def test_pokeathlon_stat_resource(self):
        base_test(self, "pokeathlon-stat")

    def test_pokemon_resource(self):
        base_test(self, "pokemon")

    def test_pokemon_color_resource(self):
        base_test(self, "pokemon-color")

    def test_pokemon_form_resource(self):
        base_test(self, "pokemon-form")

    def test_pokemon_habitat_resource(self):
        base_test(self, "pokemon-habitat")

    def test_pokemon_shape_resource(self):
        base_test(self, "pokemon-shape")

    def test_pokemon_species_resource(self):
        base_test(self, "pokemon-species")

    def test_stat_resource(self):
        base_test(self, "stat")

    def test_type_resource(self):
        base_test(self, "type")

    def test_language_resource(self):
        base_test(self, "language")


if __name__ == '__main__':
    unittest.main()
