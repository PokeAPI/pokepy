#!/usr/bin/env python
# coding: utf-8

"""
test_pokepy

Tests for pokepy module
"""

import unittest
import requests_mock
from beckett.exceptions import InvalidStatusCodeError
import pokepy


BASE_URL = 'https://pokeapi.co/api/v2'
MOCK_DATA = '{"id": "1", "name": "test_name"}'
MOCK_DATA2 = '{"id": "2", "name": "test_name2"}'


def base_get_test(self, resource, method='name'):
    """
    Base 'get' test function for V2Client

    Parameters
    ----------
    self: TestV2Client
        TestV2Client instance (self)
    resource: str
        Resource to be tested
    method: str
        'name' or 'id' (sometimes resources only have one of them)
    """
    with requests_mock.mock() as mock:
        mock.get('%s/%s/1' % (BASE_URL, resource), text=MOCK_DATA)

        # test int uid
        response_int = getattr(self.client,
                               'get_%s' % resource.replace('-', '_'))(1)[0]
        # test str uid
        response_str = getattr(self.client,
                               'get_%s' % resource.replace('-', '_'))('1')[0]

        if method == 'name':
            self.assertEqual(response_int.name, 'test_name')
            self.assertEqual(response_str.name, 'test_name')
        elif method == 'id':
            self.assertEqual(response_int.id, '1')
            self.assertEqual(response_str.id, '1')


def base_404_test(self, resource):
    """
    Base 404 error test function for V2Client

    Parameters
    ----------
    self: TestV2Client
        TestV2Client instance (self)
    resource: str
        Resource to be tested
    """
    with requests_mock.mock() as mock:
        mock.get('%s/%s/1' % (BASE_URL, resource), status_code=404)
        self.assertRaises(
            InvalidStatusCodeError,
            lambda: getattr(self.client,
                            'get_%s' % resource.replace('-', '_'))(1)[0])


def base_cache_test(self, resource):
    """
    Base cache test function for V2Client

    Parameters
    ----------
    self: TestV2ClientCacheInMemory
        TestV2ClientCacheInMemory instance (self)
    resource: str
        Resource to be tested
    """
    with requests_mock.mock() as mock:
        mock.get('%s/%s/1' % (BASE_URL, resource), text=MOCK_DATA)
        mock.get('%s/%s/2' % (BASE_URL, resource), text=MOCK_DATA2)
        resource_get_method = getattr(self.client,
                                      'get_%s' % resource.replace('-', '_'))

        # starts with 0 hits, 0 misses, and 0 cache
        self.assertEqual(resource_get_method.cache_info(), (0, 0, 0))

        # call resource
        _ = resource_get_method(1)
        # 1 miss and 1 cached
        self.assertEqual(resource_get_method.cache_info(), (0, 1, 1))

        # call same resource again
        _ = resource_get_method(1)
        # 1 hit, 1 miss, and 1 cached
        self.assertEqual(resource_get_method.cache_info(), (1, 1, 1))

        # call other resource
        _ = resource_get_method(2)
        # 1 hit, 2 miss, and 2 cached
        self.assertEqual(resource_get_method.cache_info(), (1, 2, 2))

        # clear cache
        resource_get_method.cache_clear()
        # 0 hits, 0 misses, and 0 cache
        self.assertEqual(resource_get_method.cache_info(), (0, 0, 0))

        if self.cache_type == 'in_memory':
            self.assertEqual(resource_get_method.cache_location(), 'ram')
        if self.cache_type == 'in_disk':
            self.assertEqual(resource_get_method.cache_location(), )

        # TODO não sei se faço este teste do cache_location...
        # TODO clean if in_disk
        # TODO separate str uid and int uid in different tests


class TestV2Client(unittest.TestCase):

    def setUp(self):
        self.client = pokepy.V2Client()

    def test_get_berry_resource(self):
        base_get_test(self, "berry")

    def test_get_berry_firmness_resource(self):
        base_get_test(self, "berry-firmness")

    def test_get_berry_flavor_firmness_resource(self):
        base_get_test(self, "berry-flavor")

    def test_get_contest_type_resource(self):
        base_get_test(self, "contest-type")

    def test_get_contest_effect_resource(self):
        base_get_test(self, "contest-effect", "id")

    def test_get_super_contest_effect_resource(self):
        base_get_test(self, "super-contest-effect", "id")

    def test_get_encounter_method_resource(self):
        base_get_test(self, "encounter-method")

    def test_get_encounter_condition_resource(self):
        base_get_test(self, "encounter-condition")

    def test_get_encounter_condition_value_resource(self):
        base_get_test(self, "encounter-condition-value")

    def test_get_evolution_chain_resource(self):
        base_get_test(self, "evolution-chain", "id")

    def test_get_evolution_trigger_resource(self):
        base_get_test(self, "evolution-trigger")

    def test_get_generation_resource(self):
        base_get_test(self, "generation")

    def test_get_pokedex_resource(self):
        base_get_test(self, "pokedex")

    def test_get_version_resource(self):
        base_get_test(self, "version")

    def test_get_version_group_resource(self):
        base_get_test(self, "version-group")

    def test_get_item_resource(self):
        base_get_test(self, "item")

    def test_get_item_attribute_resource(self):
        base_get_test(self, "item-attribute")

    def test_get_item_category_resource(self):
        base_get_test(self, "item-category")

    def test_get_item_fling_effect_resource(self):
        base_get_test(self, "item-fling-effect")

    def test_get_item_pocket_resource(self):
        base_get_test(self, "item-pocket")

    def test_get_machine_resource(self):
        base_get_test(self, "machine", "id")

    def test_get_move_resource(self):
        base_get_test(self, "move")

    def test_get_move_ailment_resource(self):
        base_get_test(self, "move-ailment")

    def test_get_move_battle_style_resource(self):
        base_get_test(self, "move-battle-style")

    def test_get_move_category_resource(self):
        base_get_test(self, "move-category")

    def test_get_move_damage_class_resource(self):
        base_get_test(self, "move-damage-class")

    def test_get_move_learn_method_resource(self):
        base_get_test(self, "move-learn-method")

    def test_get_move_target_resource(self):
        base_get_test(self, "move-target")

    def test_get_location_resource(self):
        base_get_test(self, "location")

    def test_get_location_area_resource(self):
        base_get_test(self, "location-area")

    def test_get_pal_park_area_resource(self):
        base_get_test(self, "pal-park-area")

    def test_get_region_resource(self):
        base_get_test(self, "region")

    def test_get_ability_resource(self):
        base_get_test(self, "ability")

    def test_get_characteristic_resource(self):
        base_get_test(self, "characteristic", "id")

    def test_get_egg_group_resource(self):
        base_get_test(self, "egg-group")

    def test_get_gender_resource(self):
        base_get_test(self, "gender")

    def test_get_growth_rate_resource(self):
        base_get_test(self, "growth-rate")

    def test_get_nature_resource(self):
        base_get_test(self, "nature")

    def test_get_pokeathlon_stat_resource(self):
        base_get_test(self, "pokeathlon-stat")

    def test_get_pokemon_resource(self):
        base_get_test(self, "pokemon")

    def test_get_pokemon_color_resource(self):
        base_get_test(self, "pokemon-color")

    def test_get_pokemon_form_resource(self):
        base_get_test(self, "pokemon-form")

    def test_get_pokemon_habitat_resource(self):
        base_get_test(self, "pokemon-habitat")

    def test_get_pokemon_shape_resource(self):
        base_get_test(self, "pokemon-shape")

    def test_get_pokemon_species_resource(self):
        base_get_test(self, "pokemon-species")

    def test_get_stat_resource(self):
        base_get_test(self, "stat")

    def test_get_type_resource(self):
        base_get_test(self, "type")

    def test_get_language_resource(self):
        base_get_test(self, "language")

    def test_404_berry_resource(self):
        base_404_test(self, "berry")

    def test_404_berry_firmness_resource(self):
        base_404_test(self, "berry-firmness")

    def test_404_berry_flavor_firmness_resource(self):
        base_404_test(self, "berry-flavor")

    def test_404_contest_type_resource(self):
        base_404_test(self, "contest-type")

    def test_404_contest_effect_resource(self):
        base_404_test(self, "contest-effect")

    def test_404_super_contest_effect_resource(self):
        base_404_test(self, "super-contest-effect")

    def test_404_encounter_method_resource(self):
        base_404_test(self, "encounter-method")

    def test_404_encounter_condition_resource(self):
        base_404_test(self, "encounter-condition")

    def test_404_encounter_condition_value_resource(self):
        base_404_test(self, "encounter-condition-value")

    def test_404_evolution_chain_resource(self):
        base_404_test(self, "evolution-chain")

    def test_404_evolution_trigger_resource(self):
        base_404_test(self, "evolution-trigger")

    def test_404_generation_resource(self):
        base_404_test(self, "generation")

    def test_404_pokedex_resource(self):
        base_404_test(self, "pokedex")

    def test_404_version_resource(self):
        base_404_test(self, "version")

    def test_404_version_group_resource(self):
        base_404_test(self, "version-group")

    def test_404_item_resource(self):
        base_404_test(self, "item")

    def test_404_item_attribute_resource(self):
        base_404_test(self, "item-attribute")

    def test_404_item_category_resource(self):
        base_404_test(self, "item-category")

    def test_404_item_fling_effect_resource(self):
        base_404_test(self, "item-fling-effect")

    def test_404_item_pocket_resource(self):
        base_404_test(self, "item-pocket")

    def test_404_machine_resource(self):
        base_404_test(self, "machine")

    def test_404_move_resource(self):
        base_404_test(self, "move")

    def test_404_move_ailment_resource(self):
        base_404_test(self, "move-ailment")

    def test_404_move_battle_style_resource(self):
        base_404_test(self, "move-battle-style")

    def test_404_move_category_resource(self):
        base_404_test(self, "move-category")

    def test_404_move_damage_class_resource(self):
        base_404_test(self, "move-damage-class")

    def test_404_move_learn_method_resource(self):
        base_404_test(self, "move-learn-method")

    def test_404_move_target_resource(self):
        base_404_test(self, "move-target")

    def test_404_location_resource(self):
        base_404_test(self, "location")

    def test_404_location_area_resource(self):
        base_404_test(self, "location-area")

    def test_404_pal_park_area_resource(self):
        base_404_test(self, "pal-park-area")

    def test_404_region_resource(self):
        base_404_test(self, "region")

    def test_404_ability_resource(self):
        base_404_test(self, "ability")

    def test_404_characteristic_resource(self):
        base_404_test(self, "characteristic")

    def test_404_egg_group_resource(self):
        base_404_test(self, "egg-group")

    def test_404_gender_resource(self):
        base_404_test(self, "gender")

    def test_404_growth_rate_resource(self):
        base_404_test(self, "growth-rate")

    def test_404_nature_resource(self):
        base_404_test(self, "nature")

    def test_404_pokeathlon_stat_resource(self):
        base_404_test(self, "pokeathlon-stat")

    def test_404_pokemon_resource(self):
        base_404_test(self, "pokemon")

    def test_404_pokemon_color_resource(self):
        base_404_test(self, "pokemon-color")

    def test_404_pokemon_form_resource(self):
        base_404_test(self, "pokemon-form")

    def test_404_pokemon_habitat_resource(self):
        base_404_test(self, "pokemon-habitat")

    def test_404_pokemon_shape_resource(self):
        base_404_test(self, "pokemon-shape")

    def test_404_pokemon_species_resource(self):
        base_404_test(self, "pokemon-species")

    def test_404_stat_resource(self):
        base_404_test(self, "stat")

    def test_404_type_resource(self):
        base_404_test(self, "type")

    def test_404_language_resource(self):
        base_404_test(self, "language")


class TestV2ClientCacheInMemory(unittest.TestCase):

    def setUp(self):
        self.client = pokepy.V2Client(cache='in_memory')
        self.cache_type = 'in_memory'

    # def test_get_berry_resource(self):
    #     base_get_test(self, "berry")


if __name__ == '__main__':
    unittest.main()
