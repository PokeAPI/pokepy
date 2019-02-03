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


base_url = 'https://pokeapi.co/api/v2'
mock_data = '{"id": "1", "name": "test_name"}'
mock_data_alternate = '{"id": "2", "name": "test_name2"}'


def base_get_test(self, resource, method='name', uid_str=True):
    """
    Base get test for 'get' methods of V2Client
    Can test str uid or int uid

    Parameters
    ----------
    self: TestV2Client
        TestV2Client instance (self)
    resource: str
        Resource to be tested
    method: str
        'name' or 'id' (sometimes resources only have one of them)
    uid_str: bool
        If True pass uid parameter as str, else pass int
    """
    with requests_mock.mock() as mock:
        mock.get('%s/%s/1' % (base_url, resource), text=mock_data)

        uid = '1' if uid_str else 1
        response = getattr(self.client, 'get_%s' % resource.replace('-', '_'))(uid)[0]

        if method == 'name':
            self.assertEqual(response.name, 'test_name')
        elif method == 'id':
            self.assertEqual(response.id, '1')


def base_repr_test(self, resource):
    """
    Base __repr__ test for 'get' methods of V2Client

    Parameters
    ----------
    self: TestV2Client
        TestV2Client instance (self)
    resource: str
        Resource to be tested
    """
    with requests_mock.mock() as mock:
        mock.get('%s/%s/1' % (base_url, resource), text=mock_data)

        response = getattr(self.client, 'get_%s' % resource.replace('-', '_'))(1)[0]
        resource_names = [name.capitalize() for name in resource.split('-')]

        self.assertTrue(
            all(char in response.__repr__() for char in ['>', '<', '-'] + resource_names))


def base_404_test(self, resource):
    """
    Base 404 error test for 'get' methods of V2Client

    Parameters
    ----------
    self: TestV2Client
        TestV2Client instance (self)
    resource: str
        Resource to be tested
    """
    with requests_mock.mock() as mock:
        mock.get('%s/%s/1' % (base_url, resource), status_code=404)
        self.assertRaises(
            InvalidStatusCodeError,
            lambda: getattr(self.client, 'get_%s' % resource.replace('-', '_'))(1)[0])


def base_cache_test(self, resource, test_to_do):
    """
    Base cache test for V2Client

    Parameters
    ----------
    self: TestV2ClientCacheInMemory
        TestV2ClientCacheInMemory instance (self)
    resource: str
        Resource to be tested
    test_to_do: str
        What cache test to perform from the following:
            'cache_info'
            'cache_clear'
            'cache_location'
    """
    with requests_mock.mock() as mock:
        mock.get('%s/%s/1' % (base_url, resource), text=mock_data)
        mock.get('%s/%s/2' % (base_url, resource), text=mock_data_alternate)
        resource_get_method = getattr(self.client, 'get_%s' % resource.replace('-', '_'))

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


class TestV2Client(unittest.TestCase):

    def setUp(self):
        self.client = pokepy.V2Client()

    def test_get_berry_str(self):
        base_get_test(self, "berry")

    def test_get_berry_firmness_str(self):
        base_get_test(self, "berry-firmness")

    def test_get_berry_flavor_str(self):
        base_get_test(self, "berry-flavor")

    def test_get_contest_type_str(self):
        base_get_test(self, "contest-type")

    def test_get_contest_effect_str(self):
        base_get_test(self, "contest-effect", "id")

    def test_get_super_contest_effect_str(self):
        base_get_test(self, "super-contest-effect", "id")

    def test_get_encounter_method_str(self):
        base_get_test(self, "encounter-method")

    def test_get_encounter_condition_str(self):
        base_get_test(self, "encounter-condition")

    def test_get_encounter_condition_value_str(self):
        base_get_test(self, "encounter-condition-value")

    def test_get_evolution_chain_str(self):
        base_get_test(self, "evolution-chain", "id")

    def test_get_evolution_trigger_str(self):
        base_get_test(self, "evolution-trigger")

    def test_get_generation_str(self):
        base_get_test(self, "generation")

    def test_get_pokedex_str(self):
        base_get_test(self, "pokedex")

    def test_get_version_str(self):
        base_get_test(self, "version")

    def test_get_version_group_str(self):
        base_get_test(self, "version-group")

    def test_get_item_str(self):
        base_get_test(self, "item")

    def test_get_item_attribute_str(self):
        base_get_test(self, "item-attribute")

    def test_get_item_category_str(self):
        base_get_test(self, "item-category")

    def test_get_item_fling_effect_str(self):
        base_get_test(self, "item-fling-effect")

    def test_get_item_pocket_str(self):
        base_get_test(self, "item-pocket")

    def test_get_machine_str(self):
        base_get_test(self, "machine", "id")

    def test_get_move_str(self):
        base_get_test(self, "move")

    def test_get_move_ailment_str(self):
        base_get_test(self, "move-ailment")

    def test_get_move_battle_style_str(self):
        base_get_test(self, "move-battle-style")

    def test_get_move_category_str(self):
        base_get_test(self, "move-category")

    def test_get_move_damage_class_str(self):
        base_get_test(self, "move-damage-class")

    def test_get_move_learn_method_str(self):
        base_get_test(self, "move-learn-method")

    def test_get_move_target_str(self):
        base_get_test(self, "move-target")

    def test_get_location_str(self):
        base_get_test(self, "location")

    def test_get_location_area_str(self):
        base_get_test(self, "location-area")

    def test_get_pal_park_area_str(self):
        base_get_test(self, "pal-park-area")

    def test_get_region_str(self):
        base_get_test(self, "region")

    def test_get_ability_str(self):
        base_get_test(self, "ability")

    def test_get_characteristic_str(self):
        base_get_test(self, "characteristic", "id")

    def test_get_egg_group_str(self):
        base_get_test(self, "egg-group")

    def test_get_gender_str(self):
        base_get_test(self, "gender")

    def test_get_growth_rate_str(self):
        base_get_test(self, "growth-rate")

    def test_get_nature_str(self):
        base_get_test(self, "nature")

    def test_get_pokeathlon_stat_str(self):
        base_get_test(self, "pokeathlon-stat")

    def test_get_pokemon_str(self):
        base_get_test(self, "pokemon")

    def test_get_pokemon_color_str(self):
        base_get_test(self, "pokemon-color")

    def test_get_pokemon_form_str(self):
        base_get_test(self, "pokemon-form")

    def test_get_pokemon_habitat_str(self):
        base_get_test(self, "pokemon-habitat")

    def test_get_pokemon_shape_str(self):
        base_get_test(self, "pokemon-shape")

    def test_get_pokemon_species_str(self):
        base_get_test(self, "pokemon-species")

    def test_get_stat_str(self):
        base_get_test(self, "stat")

    def test_get_type_str(self):
        base_get_test(self, "type")

    def test_get_language_str(self):
        base_get_test(self, "language")

    def test_get_berry_int(self):
        base_get_test(self, "berry", uid_str=False)

    def test_get_berry_firmness_int(self):
        base_get_test(self, "berry-firmness", uid_str=False)

    def test_get_berry_flavor_int(self):
        base_get_test(self, "berry-flavor", uid_str=False)

    def test_get_contest_type_int(self):
        base_get_test(self, "contest-type", uid_str=False)

    def test_get_contest_effect_int(self):
        base_get_test(self, "contest-effect", "id", False)

    def test_get_super_contest_effect_int(self):
        base_get_test(self, "super-contest-effect", "id", False)

    def test_get_encounter_method_int(self):
        base_get_test(self, "encounter-method", uid_str=False)

    def test_get_encounter_condition_int(self):
        base_get_test(self, "encounter-condition", uid_str=False)

    def test_get_encounter_condition_value_int(self):
        base_get_test(self, "encounter-condition-value", uid_str=False)

    def test_get_evolution_chain_int(self):
        base_get_test(self, "evolution-chain", "id", False)

    def test_get_evolution_trigger_int(self):
        base_get_test(self, "evolution-trigger", uid_str=False)

    def test_get_generation_int(self):
        base_get_test(self, "generation", uid_str=False)

    def test_get_pokedex_int(self):
        base_get_test(self, "pokedex", uid_str=False)

    def test_get_version_int(self):
        base_get_test(self, "version", uid_str=False)

    def test_get_version_group_int(self):
        base_get_test(self, "version-group", uid_str=False)

    def test_get_item_int(self):
        base_get_test(self, "item", uid_str=False)

    def test_get_item_attribute_int(self):
        base_get_test(self, "item-attribute", uid_str=False)

    def test_get_item_category_int(self):
        base_get_test(self, "item-category", uid_str=False)

    def test_get_item_fling_effect_int(self):
        base_get_test(self, "item-fling-effect", uid_str=False)

    def test_get_item_pocket_int(self):
        base_get_test(self, "item-pocket", uid_str=False)

    def test_get_machine_int(self):
        base_get_test(self, "machine", "id", False)

    def test_get_move_int(self):
        base_get_test(self, "move", uid_str=False)

    def test_get_move_ailment_int(self):
        base_get_test(self, "move-ailment", uid_str=False)

    def test_get_move_battle_style_int(self):
        base_get_test(self, "move-battle-style", uid_str=False)

    def test_get_move_category_int(self):
        base_get_test(self, "move-category", uid_str=False)

    def test_get_move_damage_class_int(self):
        base_get_test(self, "move-damage-class", uid_str=False)

    def test_get_move_learn_method_int(self):
        base_get_test(self, "move-learn-method", uid_str=False)

    def test_get_move_target_int(self):
        base_get_test(self, "move-target", uid_str=False)

    def test_get_location_int(self):
        base_get_test(self, "location", uid_str=False)

    def test_get_location_area_int(self):
        base_get_test(self, "location-area", uid_str=False)

    def test_get_pal_park_area_int(self):
        base_get_test(self, "pal-park-area", uid_str=False)

    def test_get_region_int(self):
        base_get_test(self, "region", uid_str=False)

    def test_get_ability_int(self):
        base_get_test(self, "ability", uid_str=False)

    def test_get_characteristic_int(self):
        base_get_test(self, "characteristic", "id", False)

    def test_get_egg_group_int(self):
        base_get_test(self, "egg-group", uid_str=False)

    def test_get_gender_int(self):
        base_get_test(self, "gender", uid_str=False)

    def test_get_growth_rate_int(self):
        base_get_test(self, "growth-rate", uid_str=False)

    def test_get_nature_int(self):
        base_get_test(self, "nature", uid_str=False)

    def test_get_pokeathlon_stat_int(self):
        base_get_test(self, "pokeathlon-stat", uid_str=False)

    def test_get_pokemon_int(self):
        base_get_test(self, "pokemon", uid_str=False)

    def test_get_pokemon_color_int(self):
        base_get_test(self, "pokemon-color", uid_str=False)

    def test_get_pokemon_form_int(self):
        base_get_test(self, "pokemon-form", uid_str=False)

    def test_get_pokemon_habitat_int(self):
        base_get_test(self, "pokemon-habitat", uid_str=False)

    def test_get_pokemon_shape_int(self):
        base_get_test(self, "pokemon-shape", uid_str=False)

    def test_get_pokemon_species_int(self):
        base_get_test(self, "pokemon-species", uid_str=False)

    def test_get_stat_int(self):
        base_get_test(self, "stat", uid_str=False)

    def test_get_type_int(self):
        base_get_test(self, "type", uid_str=False)

    def test_get_language_int(self):
        base_get_test(self, "language", uid_str=False)

    def test_get_berry_repr(self):
        base_repr_test(self, "berry")

    def test_get_berry_firmness_repr(self):
        base_repr_test(self, "berry-firmness")

    def test_get_berry_flavor_repr(self):
        base_repr_test(self, "berry-flavor")

    def test_get_contest_type_repr(self):
        base_repr_test(self, "contest-type")

    def test_get_contest_effect_repr(self):
        base_repr_test(self, "contest-effect")

    def test_get_super_contest_effect_repr(self):
        base_repr_test(self, "super-contest-effect")

    def test_get_encounter_method_repr(self):
        base_repr_test(self, "encounter-method")

    def test_get_encounter_condition_repr(self):
        base_repr_test(self, "encounter-condition")

    def test_get_encounter_condition_value_repr(self):
        base_repr_test(self, "encounter-condition-value")

    def test_get_evolution_chain_repr(self):
        base_repr_test(self, "evolution-chain")

    def test_get_evolution_trigger_repr(self):
        base_repr_test(self, "evolution-trigger")

    def test_get_generation_repr(self):
        base_repr_test(self, "generation")

    def test_get_pokedex_repr(self):
        base_repr_test(self, "pokedex")

    def test_get_version_repr(self):
        base_repr_test(self, "version")

    def test_get_version_group_repr(self):
        base_repr_test(self, "version-group")

    def test_get_item_repr(self):
        base_repr_test(self, "item")

    def test_get_item_attribute_repr(self):
        base_repr_test(self, "item-attribute")

    def test_get_item_category_repr(self):
        base_repr_test(self, "item-category")

    def test_get_item_fling_effect_repr(self):
        base_repr_test(self, "item-fling-effect")

    def test_get_item_pocket_repr(self):
        base_repr_test(self, "item-pocket")

    def test_get_machine_repr(self):
        base_repr_test(self, "machine")

    def test_get_move_repr(self):
        base_repr_test(self, "move")

    def test_get_move_ailment_repr(self):
        base_repr_test(self, "move-ailment")

    def test_get_move_battle_style_repr(self):
        base_repr_test(self, "move-battle-style")

    def test_get_move_category_repr(self):
        base_repr_test(self, "move-category")

    def test_get_move_damage_class_repr(self):
        base_repr_test(self, "move-damage-class")

    def test_get_move_learn_method_repr(self):
        base_repr_test(self, "move-learn-method")

    def test_get_move_target_repr(self):
        base_repr_test(self, "move-target")

    def test_get_location_repr(self):
        base_repr_test(self, "location")

    def test_get_location_area_repr(self):
        base_repr_test(self, "location-area")

    def test_get_pal_park_area_repr(self):
        base_repr_test(self, "pal-park-area")

    def test_get_region_repr(self):
        base_repr_test(self, "region")

    def test_get_ability_repr(self):
        base_repr_test(self, "ability")

    def test_get_characteristic_repr(self):
        base_repr_test(self, "characteristic")

    def test_get_egg_group_repr(self):
        base_repr_test(self, "egg-group")

    def test_get_gender_repr(self):
        base_repr_test(self, "gender")

    def test_get_growth_rate_repr(self):
        base_repr_test(self, "growth-rate")

    def test_get_nature_repr(self):
        base_repr_test(self, "nature")

    def test_get_pokeathlon_stat_repr(self):
        base_repr_test(self, "pokeathlon-stat")

    def test_get_pokemon_repr(self):
        base_repr_test(self, "pokemon")

    def test_get_pokemon_color_repr(self):
        base_repr_test(self, "pokemon-color")

    def test_get_pokemon_form_repr(self):
        base_repr_test(self, "pokemon-form")

    def test_get_pokemon_habitat_repr(self):
        base_repr_test(self, "pokemon-habitat")

    def test_get_pokemon_shape_repr(self):
        base_repr_test(self, "pokemon-shape")

    def test_get_pokemon_species_repr(self):
        base_repr_test(self, "pokemon-species")

    def test_get_stat_repr(self):
        base_repr_test(self, "stat")

    def test_get_type_repr(self):
        base_repr_test(self, "type")

    def test_get_language_repr(self):
        base_repr_test(self, "language")

    def test_get_berry_404(self):
        base_404_test(self, "berry")

    def test_get_berry_firmness_404(self):
        base_404_test(self, "berry-firmness")

    def test_get_berry_flavor_firmness_404(self):
        base_404_test(self, "berry-flavor")

    def test_get_contest_type_404(self):
        base_404_test(self, "contest-type")

    def test_get_contest_effect_404(self):
        base_404_test(self, "contest-effect")

    def test_get_super_contest_effect_404(self):
        base_404_test(self, "super-contest-effect")

    def test_get_encounter_method_404(self):
        base_404_test(self, "encounter-method")

    def test_get_encounter_condition_404(self):
        base_404_test(self, "encounter-condition")

    def test_get_encounter_condition_value_404(self):
        base_404_test(self, "encounter-condition-value")

    def test_get_evolution_chain_404(self):
        base_404_test(self, "evolution-chain")

    def test_get_evolution_trigger_404(self):
        base_404_test(self, "evolution-trigger")

    def test_get_generation_404(self):
        base_404_test(self, "generation")

    def test_get_pokedex_404(self):
        base_404_test(self, "pokedex")

    def test_get_version_404(self):
        base_404_test(self, "version")

    def test_get_version_group_404(self):
        base_404_test(self, "version-group")

    def test_get_item_404(self):
        base_404_test(self, "item")

    def test_get_item_attribute_404(self):
        base_404_test(self, "item-attribute")

    def test_get_item_category_404(self):
        base_404_test(self, "item-category")

    def test_get_item_fling_effect_404(self):
        base_404_test(self, "item-fling-effect")

    def test_get_item_pocket_404(self):
        base_404_test(self, "item-pocket")

    def test_get_machine_404(self):
        base_404_test(self, "machine")

    def test_get_move_404(self):
        base_404_test(self, "move")

    def test_get_move_ailment_404(self):
        base_404_test(self, "move-ailment")

    def test_get_move_battle_style_404(self):
        base_404_test(self, "move-battle-style")

    def test_get_move_category_404(self):
        base_404_test(self, "move-category")

    def test_get_move_damage_class_404(self):
        base_404_test(self, "move-damage-class")

    def test_get_move_learn_method_404(self):
        base_404_test(self, "move-learn-method")

    def test_get_move_target_404(self):
        base_404_test(self, "move-target")

    def test_get_location_404(self):
        base_404_test(self, "location")

    def test_get_location_area_404(self):
        base_404_test(self, "location-area")

    def test_get_pal_park_area_404(self):
        base_404_test(self, "pal-park-area")

    def test_get_region_404(self):
        base_404_test(self, "region")

    def test_get_ability_404(self):
        base_404_test(self, "ability")

    def test_get_characteristic_404(self):
        base_404_test(self, "characteristic")

    def test_get_egg_group_404(self):
        base_404_test(self, "egg-group")

    def test_get_gender_404(self):
        base_404_test(self, "gender")

    def test_get_growth_rate_404(self):
        base_404_test(self, "growth-rate")

    def test_get_nature_404(self):
        base_404_test(self, "nature")

    def test_get_pokeathlon_stat_404(self):
        base_404_test(self, "pokeathlon-stat")

    def test_get_pokemon_404(self):
        base_404_test(self, "pokemon")

    def test_get_pokemon_color_404(self):
        base_404_test(self, "pokemon-color")

    def test_get_pokemon_form_404(self):
        base_404_test(self, "pokemon-form")

    def test_get_pokemon_habitat_404(self):
        base_404_test(self, "pokemon-habitat")

    def test_get_pokemon_shape_404(self):
        base_404_test(self, "pokemon-shape")

    def test_get_pokemon_species_404(self):
        base_404_test(self, "pokemon-species")

    def test_get_stat_404(self):
        base_404_test(self, "stat")

    def test_get_type_404(self):
        base_404_test(self, "type")

    def test_get_language_404(self):
        base_404_test(self, "language")


class TestV2ClientCacheInMemory(unittest.TestCase):

    def setUp(self):
        self.client = pokepy.V2Client(cache='in_memory')
        self.cache_type = 'in_memory'

    # def test_get_berry_resource(self):
    #     base_get_test(self, "berry")


if __name__ == '__main__':
    unittest.main()
