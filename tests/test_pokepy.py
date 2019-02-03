#!/usr/bin/env python
# coding: utf-8

"""
test_pokepy

Tests for pokepy module
"""

import shutil
import unittest
import appdirs
import requests_mock
from beckett.exceptions import InvalidStatusCodeError
from beckett.resources import SubResource
import pokepy
from pokepy import resources_v2


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
        mock.get('%s/%s/test' % (base_url, resource), text=mock_data)
        mock.get('%s/%s/1' % (base_url, resource), text=mock_data)

        uid = 'test' if uid_str else 1
        response = getattr(self.client, 'get_%s' % resource.replace('-', '_'))(uid)[0]
        response_upper = getattr(self.client, 'get_%s' % resource.replace('-', '_'))('TEST')[0]

        if method == 'name':
            self.assertEqual(response.name, 'test_name')
            self.assertEqual(response_upper.name, 'test_name')
        elif method == 'id':
            self.assertEqual(response.id, '1')
            self.assertEqual(response_upper.id, '1')


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


def base_subresource_repr_test(self, subresource, key):
    """
    Base __repr__ test for subresources

    Parameters
    ----------
    self: TestV2Client
        TestV2Client instance (self)
    subresource: SubResources in resources_v2
        Subresource to be tested
    key: str
        key to test for
    """
    value = 'test'
    subresource_repr = subresource(**{key: value}).__repr__()

    self.assertEqual(subresource_repr, '<%s - %s>' % (subresource.Meta.name, value))


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
    self: TestV2ClientCacheInMemory or TestV2ClientCacheInDisk
        TestV2ClientCacheInMemory or TestV2ClientCacheInDisk instance (self)
    resource: str
        Resource to be tested
    test_to_do: str
        What cache test to perform from the following:
            'cache_info' - test cache_info (0 hit, 0 miss, 0 cache)
            'cache_clear' - test cache_clear (0 hit, 0 miss, 0 cache)
            'cache_location' - test cache location
            '011' - 0 hit, 1 miss, 1 cached
            '111' - 1 hit, 1 miss, 1 cached
            '022' - 0 hit, 2 miss, 2 cached
    """
    with requests_mock.mock() as mock:
        mock.get('%s/%s/1' % (base_url, resource), text=mock_data)
        mock.get('%s/%s/2' % (base_url, resource), text=mock_data_alternate)
        resource_get_method = getattr(self.client, 'get_%s' % resource.replace('-', '_'))

        if test_to_do == 'cache_info':  # starts with 0 hits, 0 misses, and 0 cache
            self.assertEqual(resource_get_method.cache_info(), (0, 0, 0))

        elif test_to_do == 'cache_clear':  # 0 hits, 0 misses, and 0 cache
            _ = resource_get_method(1)
            resource_get_method.cache_clear()
            self.assertEqual(resource_get_method.cache_info(), (0, 0, 0))

        elif test_to_do == 'cache_location':
            if self.client.cache_type == 'in_memory':
                self.assertEqual(resource_get_method.cache_location(), 'ram')
            else:  # in_disk
                self.assertTrue(
                    resource_get_method.cache_location().startswith(
                        appdirs.user_cache_dir('pokepy')))

        elif test_to_do == '011':  # 0 hits, 1 miss and 1 cached
            # call resource for the first time
            _ = resource_get_method(1)
            self.assertEqual(resource_get_method.cache_info(), (0, 1, 1))

            # clear cache for better testing
            resource_get_method.cache_clear()

        elif test_to_do == '111':  # 1 hit, 1 miss, and 1 cached
            # call same resource again
            _ = resource_get_method(1)
            _ = resource_get_method(1)
            self.assertEqual(resource_get_method.cache_info(), (1, 1, 1))

            # clear cache for better testing
            resource_get_method.cache_clear()

        elif test_to_do == '022':  # 0 hit, 2 miss, and 2 cached
            # call other resource
            _ = resource_get_method(1)
            _ = resource_get_method(2)
            self.assertEqual(resource_get_method.cache_info(), (0, 2, 2))

            # clear cache for better testing
            resource_get_method.cache_clear()


class TestV2Client(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = pokepy.V2Client()

    # uid str

    def test_get_berry_str(self):
        base_get_test(self, 'berry')

    def test_get_berry_firmness_str(self):
        base_get_test(self, 'berry-firmness')

    def test_get_berry_flavor_str(self):
        base_get_test(self, 'berry-flavor')

    def test_get_contest_type_str(self):
        base_get_test(self, 'contest-type')

    def test_get_contest_effect_str(self):
        base_get_test(self, 'contest-effect', 'id')

    def test_get_super_contest_effect_str(self):
        base_get_test(self, 'super-contest-effect', 'id')

    def test_get_encounter_method_str(self):
        base_get_test(self, 'encounter-method')

    def test_get_encounter_condition_str(self):
        base_get_test(self, 'encounter-condition')

    def test_get_encounter_condition_value_str(self):
        base_get_test(self, 'encounter-condition-value')

    def test_get_evolution_chain_str(self):
        base_get_test(self, 'evolution-chain', 'id')

    def test_get_evolution_trigger_str(self):
        base_get_test(self, 'evolution-trigger')

    def test_get_generation_str(self):
        base_get_test(self, 'generation')

    def test_get_pokedex_str(self):
        base_get_test(self, 'pokedex')

    def test_get_version_str(self):
        base_get_test(self, 'version')

    def test_get_version_group_str(self):
        base_get_test(self, 'version-group')

    def test_get_item_str(self):
        base_get_test(self, 'item')

    def test_get_item_attribute_str(self):
        base_get_test(self, 'item-attribute')

    def test_get_item_category_str(self):
        base_get_test(self, 'item-category')

    def test_get_item_fling_effect_str(self):
        base_get_test(self, 'item-fling-effect')

    def test_get_item_pocket_str(self):
        base_get_test(self, 'item-pocket')

    def test_get_machine_str(self):
        base_get_test(self, 'machine', 'id')

    def test_get_move_str(self):
        base_get_test(self, 'move')

    def test_get_move_ailment_str(self):
        base_get_test(self, 'move-ailment')

    def test_get_move_battle_style_str(self):
        base_get_test(self, 'move-battle-style')

    def test_get_move_category_str(self):
        base_get_test(self, 'move-category')

    def test_get_move_damage_class_str(self):
        base_get_test(self, 'move-damage-class')

    def test_get_move_learn_method_str(self):
        base_get_test(self, 'move-learn-method')

    def test_get_move_target_str(self):
        base_get_test(self, 'move-target')

    def test_get_location_str(self):
        base_get_test(self, 'location')

    def test_get_location_area_str(self):
        base_get_test(self, 'location-area')

    def test_get_pal_park_area_str(self):
        base_get_test(self, 'pal-park-area')

    def test_get_region_str(self):
        base_get_test(self, 'region')

    def test_get_ability_str(self):
        base_get_test(self, 'ability')

    def test_get_characteristic_str(self):
        base_get_test(self, 'characteristic', 'id')

    def test_get_egg_group_str(self):
        base_get_test(self, 'egg-group')

    def test_get_gender_str(self):
        base_get_test(self, 'gender')

    def test_get_growth_rate_str(self):
        base_get_test(self, 'growth-rate')

    def test_get_nature_str(self):
        base_get_test(self, 'nature')

    def test_get_pokeathlon_stat_str(self):
        base_get_test(self, 'pokeathlon-stat')

    def test_get_pokemon_str(self):
        base_get_test(self, 'pokemon')

    def test_get_pokemon_color_str(self):
        base_get_test(self, 'pokemon-color')

    def test_get_pokemon_form_str(self):
        base_get_test(self, 'pokemon-form')

    def test_get_pokemon_habitat_str(self):
        base_get_test(self, 'pokemon-habitat')

    def test_get_pokemon_shape_str(self):
        base_get_test(self, 'pokemon-shape')

    def test_get_pokemon_species_str(self):
        base_get_test(self, 'pokemon-species')

    def test_get_stat_str(self):
        base_get_test(self, 'stat')

    def test_get_type_str(self):
        base_get_test(self, 'type')

    def test_get_language_str(self):
        base_get_test(self, 'language')

    # uid int

    def test_get_berry_int(self):
        base_get_test(self, 'berry', uid_str=False)

    def test_get_berry_firmness_int(self):
        base_get_test(self, 'berry-firmness', uid_str=False)

    def test_get_berry_flavor_int(self):
        base_get_test(self, 'berry-flavor', uid_str=False)

    def test_get_contest_type_int(self):
        base_get_test(self, 'contest-type', uid_str=False)

    def test_get_contest_effect_int(self):
        base_get_test(self, 'contest-effect', 'id', False)

    def test_get_super_contest_effect_int(self):
        base_get_test(self, 'super-contest-effect', 'id', False)

    def test_get_encounter_method_int(self):
        base_get_test(self, 'encounter-method', uid_str=False)

    def test_get_encounter_condition_int(self):
        base_get_test(self, 'encounter-condition', uid_str=False)

    def test_get_encounter_condition_value_int(self):
        base_get_test(self, 'encounter-condition-value', uid_str=False)

    def test_get_evolution_chain_int(self):
        base_get_test(self, 'evolution-chain', 'id', False)

    def test_get_evolution_trigger_int(self):
        base_get_test(self, 'evolution-trigger', uid_str=False)

    def test_get_generation_int(self):
        base_get_test(self, 'generation', uid_str=False)

    def test_get_pokedex_int(self):
        base_get_test(self, 'pokedex', uid_str=False)

    def test_get_version_int(self):
        base_get_test(self, 'version', uid_str=False)

    def test_get_version_group_int(self):
        base_get_test(self, 'version-group', uid_str=False)

    def test_get_item_int(self):
        base_get_test(self, 'item', uid_str=False)

    def test_get_item_attribute_int(self):
        base_get_test(self, 'item-attribute', uid_str=False)

    def test_get_item_category_int(self):
        base_get_test(self, 'item-category', uid_str=False)

    def test_get_item_fling_effect_int(self):
        base_get_test(self, 'item-fling-effect', uid_str=False)

    def test_get_item_pocket_int(self):
        base_get_test(self, 'item-pocket', uid_str=False)

    def test_get_machine_int(self):
        base_get_test(self, 'machine', 'id', False)

    def test_get_move_int(self):
        base_get_test(self, 'move', uid_str=False)

    def test_get_move_ailment_int(self):
        base_get_test(self, 'move-ailment', uid_str=False)

    def test_get_move_battle_style_int(self):
        base_get_test(self, 'move-battle-style', uid_str=False)

    def test_get_move_category_int(self):
        base_get_test(self, 'move-category', uid_str=False)

    def test_get_move_damage_class_int(self):
        base_get_test(self, 'move-damage-class', uid_str=False)

    def test_get_move_learn_method_int(self):
        base_get_test(self, 'move-learn-method', uid_str=False)

    def test_get_move_target_int(self):
        base_get_test(self, 'move-target', uid_str=False)

    def test_get_location_int(self):
        base_get_test(self, 'location', uid_str=False)

    def test_get_location_area_int(self):
        base_get_test(self, 'location-area', uid_str=False)

    def test_get_pal_park_area_int(self):
        base_get_test(self, 'pal-park-area', uid_str=False)

    def test_get_region_int(self):
        base_get_test(self, 'region', uid_str=False)

    def test_get_ability_int(self):
        base_get_test(self, 'ability', uid_str=False)

    def test_get_characteristic_int(self):
        base_get_test(self, 'characteristic', 'id', False)

    def test_get_egg_group_int(self):
        base_get_test(self, 'egg-group', uid_str=False)

    def test_get_gender_int(self):
        base_get_test(self, 'gender', uid_str=False)

    def test_get_growth_rate_int(self):
        base_get_test(self, 'growth-rate', uid_str=False)

    def test_get_nature_int(self):
        base_get_test(self, 'nature', uid_str=False)

    def test_get_pokeathlon_stat_int(self):
        base_get_test(self, 'pokeathlon-stat', uid_str=False)

    def test_get_pokemon_int(self):
        base_get_test(self, 'pokemon', uid_str=False)

    def test_get_pokemon_color_int(self):
        base_get_test(self, 'pokemon-color', uid_str=False)

    def test_get_pokemon_form_int(self):
        base_get_test(self, 'pokemon-form', uid_str=False)

    def test_get_pokemon_habitat_int(self):
        base_get_test(self, 'pokemon-habitat', uid_str=False)

    def test_get_pokemon_shape_int(self):
        base_get_test(self, 'pokemon-shape', uid_str=False)

    def test_get_pokemon_species_int(self):
        base_get_test(self, 'pokemon-species', uid_str=False)

    def test_get_stat_int(self):
        base_get_test(self, 'stat', uid_str=False)

    def test_get_type_int(self):
        base_get_test(self, 'type', uid_str=False)

    def test_get_language_int(self):
        base_get_test(self, 'language', uid_str=False)

    # __repr__

    def test_APIResourceSubResource_repr(self):
        base_subresource_repr_test(self, resources_v2.APIResourceSubResource, 'url')

    # TODO

    def test_get_berry_repr(self):
        base_repr_test(self, 'berry')

    def test_get_berry_firmness_repr(self):
        base_repr_test(self, 'berry-firmness')

    def test_get_berry_flavor_repr(self):
        base_repr_test(self, 'berry-flavor')

    def test_get_contest_type_repr(self):
        base_repr_test(self, 'contest-type')

    def test_get_contest_effect_repr(self):
        base_repr_test(self, 'contest-effect')

    def test_get_super_contest_effect_repr(self):
        base_repr_test(self, 'super-contest-effect')

    def test_get_encounter_method_repr(self):
        base_repr_test(self, 'encounter-method')

    def test_get_encounter_condition_repr(self):
        base_repr_test(self, 'encounter-condition')

    def test_get_encounter_condition_value_repr(self):
        base_repr_test(self, 'encounter-condition-value')

    def test_get_evolution_chain_repr(self):
        base_repr_test(self, 'evolution-chain')

    def test_get_evolution_trigger_repr(self):
        base_repr_test(self, 'evolution-trigger')

    def test_get_generation_repr(self):
        base_repr_test(self, 'generation')

    def test_get_pokedex_repr(self):
        base_repr_test(self, 'pokedex')

    def test_get_version_repr(self):
        base_repr_test(self, 'version')

    def test_get_version_group_repr(self):
        base_repr_test(self, 'version-group')

    def test_get_item_repr(self):
        base_repr_test(self, 'item')

    def test_get_item_attribute_repr(self):
        base_repr_test(self, 'item-attribute')

    def test_get_item_category_repr(self):
        base_repr_test(self, 'item-category')

    def test_get_item_fling_effect_repr(self):
        base_repr_test(self, 'item-fling-effect')

    def test_get_item_pocket_repr(self):
        base_repr_test(self, 'item-pocket')

    def test_get_machine_repr(self):
        base_repr_test(self, 'machine')

    def test_get_move_repr(self):
        base_repr_test(self, 'move')

    def test_get_move_ailment_repr(self):
        base_repr_test(self, 'move-ailment')

    def test_get_move_battle_style_repr(self):
        base_repr_test(self, 'move-battle-style')

    def test_get_move_category_repr(self):
        base_repr_test(self, 'move-category')

    def test_get_move_damage_class_repr(self):
        base_repr_test(self, 'move-damage-class')

    def test_get_move_learn_method_repr(self):
        base_repr_test(self, 'move-learn-method')

    def test_get_move_target_repr(self):
        base_repr_test(self, 'move-target')

    def test_get_location_repr(self):
        base_repr_test(self, 'location')

    def test_get_location_area_repr(self):
        base_repr_test(self, 'location-area')

    def test_get_pal_park_area_repr(self):
        base_repr_test(self, 'pal-park-area')

    def test_get_region_repr(self):
        base_repr_test(self, 'region')

    def test_get_ability_repr(self):
        base_repr_test(self, 'ability')

    def test_get_characteristic_repr(self):
        base_repr_test(self, 'characteristic')

    def test_get_egg_group_repr(self):
        base_repr_test(self, 'egg-group')

    def test_get_gender_repr(self):
        base_repr_test(self, 'gender')

    def test_get_growth_rate_repr(self):
        base_repr_test(self, 'growth-rate')

    def test_get_nature_repr(self):
        base_repr_test(self, 'nature')

    def test_get_pokeathlon_stat_repr(self):
        base_repr_test(self, 'pokeathlon-stat')

    def test_get_pokemon_repr(self):
        base_repr_test(self, 'pokemon')

    def test_get_pokemon_color_repr(self):
        base_repr_test(self, 'pokemon-color')

    def test_get_pokemon_form_repr(self):
        base_repr_test(self, 'pokemon-form')

    def test_get_pokemon_habitat_repr(self):
        base_repr_test(self, 'pokemon-habitat')

    def test_get_pokemon_shape_repr(self):
        base_repr_test(self, 'pokemon-shape')

    def test_get_pokemon_species_repr(self):
        base_repr_test(self, 'pokemon-species')

    def test_get_stat_repr(self):
        base_repr_test(self, 'stat')

    def test_get_type_repr(self):
        base_repr_test(self, 'type')

    def test_get_language_repr(self):
        base_repr_test(self, 'language')

    # 404

    def test_get_berry_404(self):
        base_404_test(self, 'berry')

    def test_get_berry_firmness_404(self):
        base_404_test(self, 'berry-firmness')

    def test_get_berry_flavor_firmness_404(self):
        base_404_test(self, 'berry-flavor')

    def test_get_contest_type_404(self):
        base_404_test(self, 'contest-type')

    def test_get_contest_effect_404(self):
        base_404_test(self, 'contest-effect')

    def test_get_super_contest_effect_404(self):
        base_404_test(self, 'super-contest-effect')

    def test_get_encounter_method_404(self):
        base_404_test(self, 'encounter-method')

    def test_get_encounter_condition_404(self):
        base_404_test(self, 'encounter-condition')

    def test_get_encounter_condition_value_404(self):
        base_404_test(self, 'encounter-condition-value')

    def test_get_evolution_chain_404(self):
        base_404_test(self, 'evolution-chain')

    def test_get_evolution_trigger_404(self):
        base_404_test(self, 'evolution-trigger')

    def test_get_generation_404(self):
        base_404_test(self, 'generation')

    def test_get_pokedex_404(self):
        base_404_test(self, 'pokedex')

    def test_get_version_404(self):
        base_404_test(self, 'version')

    def test_get_version_group_404(self):
        base_404_test(self, 'version-group')

    def test_get_item_404(self):
        base_404_test(self, 'item')

    def test_get_item_attribute_404(self):
        base_404_test(self, 'item-attribute')

    def test_get_item_category_404(self):
        base_404_test(self, 'item-category')

    def test_get_item_fling_effect_404(self):
        base_404_test(self, 'item-fling-effect')

    def test_get_item_pocket_404(self):
        base_404_test(self, 'item-pocket')

    def test_get_machine_404(self):
        base_404_test(self, 'machine')

    def test_get_move_404(self):
        base_404_test(self, 'move')

    def test_get_move_ailment_404(self):
        base_404_test(self, 'move-ailment')

    def test_get_move_battle_style_404(self):
        base_404_test(self, 'move-battle-style')

    def test_get_move_category_404(self):
        base_404_test(self, 'move-category')

    def test_get_move_damage_class_404(self):
        base_404_test(self, 'move-damage-class')

    def test_get_move_learn_method_404(self):
        base_404_test(self, 'move-learn-method')

    def test_get_move_target_404(self):
        base_404_test(self, 'move-target')

    def test_get_location_404(self):
        base_404_test(self, 'location')

    def test_get_location_area_404(self):
        base_404_test(self, 'location-area')

    def test_get_pal_park_area_404(self):
        base_404_test(self, 'pal-park-area')

    def test_get_region_404(self):
        base_404_test(self, 'region')

    def test_get_ability_404(self):
        base_404_test(self, 'ability')

    def test_get_characteristic_404(self):
        base_404_test(self, 'characteristic')

    def test_get_egg_group_404(self):
        base_404_test(self, 'egg-group')

    def test_get_gender_404(self):
        base_404_test(self, 'gender')

    def test_get_growth_rate_404(self):
        base_404_test(self, 'growth-rate')

    def test_get_nature_404(self):
        base_404_test(self, 'nature')

    def test_get_pokeathlon_stat_404(self):
        base_404_test(self, 'pokeathlon-stat')

    def test_get_pokemon_404(self):
        base_404_test(self, 'pokemon')

    def test_get_pokemon_color_404(self):
        base_404_test(self, 'pokemon-color')

    def test_get_pokemon_form_404(self):
        base_404_test(self, 'pokemon-form')

    def test_get_pokemon_habitat_404(self):
        base_404_test(self, 'pokemon-habitat')

    def test_get_pokemon_shape_404(self):
        base_404_test(self, 'pokemon-shape')

    def test_get_pokemon_species_404(self):
        base_404_test(self, 'pokemon-species')

    def test_get_stat_404(self):
        base_404_test(self, 'stat')

    def test_get_type_404(self):
        base_404_test(self, 'type')

    def test_get_language_404(self):
        base_404_test(self, 'language')


class TestV2ClientCacheInMemory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = pokepy.V2Client(cache='in_memory')

    def test_cache_type(self):
        self.assertEqual(self.client.cache_type, 'in_memory')

    # cache_info

    def test_get_berry_cache_info(self):
        base_cache_test(self, 'berry', 'cache_info')

    def test_get_berry_firmness_cache_info(self):
        base_cache_test(self, 'berry-firmness', 'cache_info')

    def test_get_berry_flavor_cache_info(self):
        base_cache_test(self, 'berry-flavor', 'cache_info')

    def test_get_contest_type_cache_info(self):
        base_cache_test(self, 'contest-type', 'cache_info')

    def test_get_contest_effect_cache_info(self):
        base_cache_test(self, 'contest-effect', 'cache_info')

    def test_get_super_contest_effect_cache_info(self):
        base_cache_test(self, 'super-contest-effect', 'cache_info')

    def test_get_encounter_method_cache_info(self):
        base_cache_test(self, 'encounter-method', 'cache_info')

    def test_get_encounter_condition_cache_info(self):
        base_cache_test(self, 'encounter-condition', 'cache_info')

    def test_get_encounter_condition_value_cache_info(self):
        base_cache_test(self, 'encounter-condition-value', 'cache_info')

    def test_get_evolution_chain_cache_info(self):
        base_cache_test(self, 'evolution-chain', 'cache_info')

    def test_get_evolution_trigger_cache_info(self):
        base_cache_test(self, 'evolution-trigger', 'cache_info')

    def test_get_generation_cache_info(self):
        base_cache_test(self, 'generation', 'cache_info')

    def test_get_pokedex_cache_info(self):
        base_cache_test(self, 'pokedex', 'cache_info')

    def test_get_version_cache_info(self):
        base_cache_test(self, 'version', 'cache_info')

    def test_get_version_group_cache_info(self):
        base_cache_test(self, 'version-group', 'cache_info')

    def test_get_item_cache_info(self):
        base_cache_test(self, 'item', 'cache_info')

    def test_get_item_attribute_cache_info(self):
        base_cache_test(self, 'item-attribute', 'cache_info')

    def test_get_item_category_cache_info(self):
        base_cache_test(self, 'item-category', 'cache_info')

    def test_get_item_fling_effect_cache_info(self):
        base_cache_test(self, 'item-fling-effect', 'cache_info')

    def test_get_item_pocket_cache_info(self):
        base_cache_test(self, 'item-pocket', 'cache_info')

    def test_get_machine_cache_info(self):
        base_cache_test(self, 'machine', 'cache_info')

    def test_get_move_cache_info(self):
        base_cache_test(self, 'move', 'cache_info')

    def test_get_move_ailment_cache_info(self):
        base_cache_test(self, 'move-ailment', 'cache_info')

    def test_get_move_battle_style_cache_info(self):
        base_cache_test(self, 'move-battle-style', 'cache_info')

    def test_get_move_category_cache_info(self):
        base_cache_test(self, 'move-category', 'cache_info')

    def test_get_move_damage_class_cache_info(self):
        base_cache_test(self, 'move-damage-class', 'cache_info')

    def test_get_move_learn_method_cache_info(self):
        base_cache_test(self, 'move-learn-method', 'cache_info')

    def test_get_move_target_cache_info(self):
        base_cache_test(self, 'move-target', 'cache_info')

    def test_get_location_cache_info(self):
        base_cache_test(self, 'location', 'cache_info')

    def test_get_location_area_cache_info(self):
        base_cache_test(self, 'location-area', 'cache_info')

    def test_get_pal_park_area_cache_info(self):
        base_cache_test(self, 'pal-park-area', 'cache_info')

    def test_get_region_cache_info(self):
        base_cache_test(self, 'region', 'cache_info')

    def test_get_ability_cache_info(self):
        base_cache_test(self, 'ability', 'cache_info')

    def test_get_characteristic_cache_info(self):
        base_cache_test(self, 'characteristic', 'cache_info')

    def test_get_egg_group_cache_info(self):
        base_cache_test(self, 'egg-group', 'cache_info')

    def test_get_gender_cache_info(self):
        base_cache_test(self, 'gender', 'cache_info')

    def test_get_growth_rate_cache_info(self):
        base_cache_test(self, 'growth-rate', 'cache_info')

    def test_get_nature_cache_info(self):
        base_cache_test(self, 'nature', 'cache_info')

    def test_get_pokeathlon_stat_cache_info(self):
        base_cache_test(self, 'pokeathlon-stat', 'cache_info')

    def test_get_pokemon_cache_info(self):
        base_cache_test(self, 'pokemon', 'cache_info')

    def test_get_pokemon_color_cache_info(self):
        base_cache_test(self, 'pokemon-color', 'cache_info')

    def test_get_pokemon_form_cache_info(self):
        base_cache_test(self, 'pokemon-form', 'cache_info')

    def test_get_pokemon_habitat_cache_info(self):
        base_cache_test(self, 'pokemon-habitat', 'cache_info')

    def test_get_pokemon_shape_cache_info(self):
        base_cache_test(self, 'pokemon-shape', 'cache_info')

    def test_get_pokemon_species_cache_info(self):
        base_cache_test(self, 'pokemon-species', 'cache_info')

    def test_get_stat_cache_info(self):
        base_cache_test(self, 'stat', 'cache_info')

    def test_get_type_cache_info(self):
        base_cache_test(self, 'type', 'cache_info')

    def test_get_language_cache_info(self):
        base_cache_test(self, 'language', 'cache_info')

    # cache_clear

    def test_get_berry_cache_clear(self):
        base_cache_test(self, "berry", 'cache_clear')

    def test_get_berry_firmness_cache_clear(self):
        base_cache_test(self, "berry-firmness", 'cache_clear')

    def test_get_berry_flavor_cache_clear(self):
        base_cache_test(self, "berry-flavor", 'cache_clear')

    def test_get_contest_type_cache_clear(self):
        base_cache_test(self, "contest-type", 'cache_clear')

    def test_get_contest_effect_cache_clear(self):
        base_cache_test(self, "contest-effect", 'cache_clear')

    def test_get_super_contest_effect_cache_clear(self):
        base_cache_test(self, "super-contest-effect", 'cache_clear')

    def test_get_encounter_method_cache_clear(self):
        base_cache_test(self, "encounter-method", 'cache_clear')

    def test_get_encounter_condition_cache_clear(self):
        base_cache_test(self, "encounter-condition", 'cache_clear')

    def test_get_encounter_condition_value_cache_clear(self):
        base_cache_test(self, "encounter-condition-value", 'cache_clear')

    def test_get_evolution_chain_cache_clear(self):
        base_cache_test(self, "evolution-chain", 'cache_clear')

    def test_get_evolution_trigger_cache_clear(self):
        base_cache_test(self, "evolution-trigger", 'cache_clear')

    def test_get_generation_cache_clear(self):
        base_cache_test(self, "generation", 'cache_clear')

    def test_get_pokedex_cache_clear(self):
        base_cache_test(self, "pokedex", 'cache_clear')

    def test_get_version_cache_clear(self):
        base_cache_test(self, "version", 'cache_clear')

    def test_get_version_group_cache_clear(self):
        base_cache_test(self, "version-group", 'cache_clear')

    def test_get_item_cache_clear(self):
        base_cache_test(self, "item", 'cache_clear')

    def test_get_item_attribute_cache_clear(self):
        base_cache_test(self, "item-attribute", 'cache_clear')

    def test_get_item_category_cache_clear(self):
        base_cache_test(self, "item-category", 'cache_clear')

    def test_get_item_fling_effect_cache_clear(self):
        base_cache_test(self, "item-fling-effect", 'cache_clear')

    def test_get_item_pocket_cache_clear(self):
        base_cache_test(self, "item-pocket", 'cache_clear')

    def test_get_machine_cache_clear(self):
        base_cache_test(self, "machine", 'cache_clear')

    def test_get_move_cache_clear(self):
        base_cache_test(self, "move", 'cache_clear')

    def test_get_move_ailment_cache_clear(self):
        base_cache_test(self, "move-ailment", 'cache_clear')

    def test_get_move_battle_style_cache_clear(self):
        base_cache_test(self, "move-battle-style", 'cache_clear')

    def test_get_move_category_cache_clear(self):
        base_cache_test(self, "move-category", 'cache_clear')

    def test_get_move_damage_class_cache_clear(self):
        base_cache_test(self, "move-damage-class", 'cache_clear')

    def test_get_move_learn_method_cache_clear(self):
        base_cache_test(self, "move-learn-method", 'cache_clear')

    def test_get_move_target_cache_clear(self):
        base_cache_test(self, "move-target", 'cache_clear')

    def test_get_location_cache_clear(self):
        base_cache_test(self, "location", 'cache_clear')

    def test_get_location_area_cache_clear(self):
        base_cache_test(self, "location-area", 'cache_clear')

    def test_get_pal_park_area_cache_clear(self):
        base_cache_test(self, "pal-park-area", 'cache_clear')

    def test_get_region_cache_clear(self):
        base_cache_test(self, "region", 'cache_clear')

    def test_get_ability_cache_clear(self):
        base_cache_test(self, "ability", 'cache_clear')

    def test_get_characteristic_cache_clear(self):
        base_cache_test(self, "characteristic", 'cache_clear')

    def test_get_egg_group_cache_clear(self):
        base_cache_test(self, "egg-group", 'cache_clear')

    def test_get_gender_cache_clear(self):
        base_cache_test(self, "gender", 'cache_clear')

    def test_get_growth_rate_cache_clear(self):
        base_cache_test(self, "growth-rate", 'cache_clear')

    def test_get_nature_cache_clear(self):
        base_cache_test(self, "nature", 'cache_clear')

    def test_get_pokeathlon_stat_cache_clear(self):
        base_cache_test(self, "pokeathlon-stat", 'cache_clear')

    def test_get_pokemon_cache_clear(self):
        base_cache_test(self, "pokemon", 'cache_clear')

    def test_get_pokemon_color_cache_clear(self):
        base_cache_test(self, "pokemon-color", 'cache_clear')

    def test_get_pokemon_form_cache_clear(self):
        base_cache_test(self, "pokemon-form", 'cache_clear')

    def test_get_pokemon_habitat_cache_clear(self):
        base_cache_test(self, "pokemon-habitat", 'cache_clear')

    def test_get_pokemon_shape_cache_clear(self):
        base_cache_test(self, "pokemon-shape", 'cache_clear')

    def test_get_pokemon_species_cache_clear(self):
        base_cache_test(self, "pokemon-species", 'cache_clear')

    def test_get_stat_cache_clear(self):
        base_cache_test(self, "stat", 'cache_clear')

    def test_get_type_cache_clear(self):
        base_cache_test(self, "type", 'cache_clear')

    def test_get_language_cache_clear(self):
        base_cache_test(self, "language", 'cache_clear')

    # cache_location

    def test_get_berry_cache_location(self):
        base_cache_test(self, "berry", 'cache_location')

    def test_get_berry_firmness_cache_location(self):
        base_cache_test(self, "berry-firmness", 'cache_location')

    def test_get_berry_flavor_cache_location(self):
        base_cache_test(self, "berry-flavor", 'cache_location')

    def test_get_contest_type_cache_location(self):
        base_cache_test(self, "contest-type", 'cache_location')

    def test_get_contest_effect_cache_location(self):
        base_cache_test(self, "contest-effect", 'cache_location')

    def test_get_super_contest_effect_cache_location(self):
        base_cache_test(self, "super-contest-effect", 'cache_location')

    def test_get_encounter_method_cache_location(self):
        base_cache_test(self, "encounter-method", 'cache_location')

    def test_get_encounter_condition_cache_location(self):
        base_cache_test(self, "encounter-condition", 'cache_location')

    def test_get_encounter_condition_value_cache_location(self):
        base_cache_test(self, "encounter-condition-value", 'cache_location')

    def test_get_evolution_chain_cache_location(self):
        base_cache_test(self, "evolution-chain", 'cache_location')

    def test_get_evolution_trigger_cache_location(self):
        base_cache_test(self, "evolution-trigger", 'cache_location')

    def test_get_generation_cache_location(self):
        base_cache_test(self, "generation", 'cache_location')

    def test_get_pokedex_cache_location(self):
        base_cache_test(self, "pokedex", 'cache_location')

    def test_get_version_cache_location(self):
        base_cache_test(self, "version", 'cache_location')

    def test_get_version_group_cache_location(self):
        base_cache_test(self, "version-group", 'cache_location')

    def test_get_item_cache_location(self):
        base_cache_test(self, "item", 'cache_location')

    def test_get_item_attribute_cache_location(self):
        base_cache_test(self, "item-attribute", 'cache_location')

    def test_get_item_category_cache_location(self):
        base_cache_test(self, "item-category", 'cache_location')

    def test_get_item_fling_effect_cache_location(self):
        base_cache_test(self, "item-fling-effect", 'cache_location')

    def test_get_item_pocket_cache_location(self):
        base_cache_test(self, "item-pocket", 'cache_location')

    def test_get_machine_cache_location(self):
        base_cache_test(self, "machine", 'cache_location')

    def test_get_move_cache_location(self):
        base_cache_test(self, "move", 'cache_location')

    def test_get_move_ailment_cache_location(self):
        base_cache_test(self, "move-ailment", 'cache_location')

    def test_get_move_battle_style_cache_location(self):
        base_cache_test(self, "move-battle-style", 'cache_location')

    def test_get_move_category_cache_location(self):
        base_cache_test(self, "move-category", 'cache_location')

    def test_get_move_damage_class_cache_location(self):
        base_cache_test(self, "move-damage-class", 'cache_location')

    def test_get_move_learn_method_cache_location(self):
        base_cache_test(self, "move-learn-method", 'cache_location')

    def test_get_move_target_cache_location(self):
        base_cache_test(self, "move-target", 'cache_location')

    def test_get_location_cache_location(self):
        base_cache_test(self, "location", 'cache_location')

    def test_get_location_area_cache_location(self):
        base_cache_test(self, "location-area", 'cache_location')

    def test_get_pal_park_area_cache_location(self):
        base_cache_test(self, "pal-park-area", 'cache_location')

    def test_get_region_cache_location(self):
        base_cache_test(self, "region", 'cache_location')

    def test_get_ability_cache_location(self):
        base_cache_test(self, "ability", 'cache_location')

    def test_get_characteristic_cache_location(self):
        base_cache_test(self, "characteristic", 'cache_location')

    def test_get_egg_group_cache_location(self):
        base_cache_test(self, "egg-group", 'cache_location')

    def test_get_gender_cache_location(self):
        base_cache_test(self, "gender", 'cache_location')

    def test_get_growth_rate_cache_location(self):
        base_cache_test(self, "growth-rate", 'cache_location')

    def test_get_nature_cache_location(self):
        base_cache_test(self, "nature", 'cache_location')

    def test_get_pokeathlon_stat_cache_location(self):
        base_cache_test(self, "pokeathlon-stat", 'cache_location')

    def test_get_pokemon_cache_location(self):
        base_cache_test(self, "pokemon", 'cache_location')

    def test_get_pokemon_color_cache_location(self):
        base_cache_test(self, "pokemon-color", 'cache_location')

    def test_get_pokemon_form_cache_location(self):
        base_cache_test(self, "pokemon-form", 'cache_location')

    def test_get_pokemon_habitat_cache_location(self):
        base_cache_test(self, "pokemon-habitat", 'cache_location')

    def test_get_pokemon_shape_cache_location(self):
        base_cache_test(self, "pokemon-shape", 'cache_location')

    def test_get_pokemon_species_cache_location(self):
        base_cache_test(self, "pokemon-species", 'cache_location')

    def test_get_stat_cache_location(self):
        base_cache_test(self, "stat", 'cache_location')

    def test_get_type_cache_location(self):
        base_cache_test(self, "type", 'cache_location')

    def test_get_language_cache_location(self):
        base_cache_test(self, "language", 'cache_location')

    # 011 - 0 hit, 1 miss, 1 cached

    def test_get_berry_011(self):
        base_cache_test(self, "berry", '011')

    def test_get_berry_firmness_011(self):
        base_cache_test(self, "berry-firmness", '011')

    def test_get_berry_flavor_011(self):
        base_cache_test(self, "berry-flavor", '011')

    def test_get_contest_type_011(self):
        base_cache_test(self, "contest-type", '011')

    def test_get_contest_effect_011(self):
        base_cache_test(self, "contest-effect", '011')

    def test_get_super_contest_effect_011(self):
        base_cache_test(self, "super-contest-effect", '011')

    def test_get_encounter_method_011(self):
        base_cache_test(self, "encounter-method", '011')

    def test_get_encounter_condition_011(self):
        base_cache_test(self, "encounter-condition", '011')

    def test_get_encounter_condition_value_011(self):
        base_cache_test(self, "encounter-condition-value", '011')

    def test_get_evolution_chain_011(self):
        base_cache_test(self, "evolution-chain", '011')

    def test_get_evolution_trigger_011(self):
        base_cache_test(self, "evolution-trigger", '011')

    def test_get_generation_011(self):
        base_cache_test(self, "generation", '011')

    def test_get_pokedex_011(self):
        base_cache_test(self, "pokedex", '011')

    def test_get_version_011(self):
        base_cache_test(self, "version", '011')

    def test_get_version_group_011(self):
        base_cache_test(self, "version-group", '011')

    def test_get_item_011(self):
        base_cache_test(self, "item", '011')

    def test_get_item_attribute_011(self):
        base_cache_test(self, "item-attribute", '011')

    def test_get_item_category_011(self):
        base_cache_test(self, "item-category", '011')

    def test_get_item_fling_effect_011(self):
        base_cache_test(self, "item-fling-effect", '011')

    def test_get_item_pocket_011(self):
        base_cache_test(self, "item-pocket", '011')

    def test_get_machine_011(self):
        base_cache_test(self, "machine", '011')

    def test_get_move_011(self):
        base_cache_test(self, "move", '011')

    def test_get_move_ailment_011(self):
        base_cache_test(self, "move-ailment", '011')

    def test_get_move_battle_style_011(self):
        base_cache_test(self, "move-battle-style", '011')

    def test_get_move_category_011(self):
        base_cache_test(self, "move-category", '011')

    def test_get_move_damage_class_011(self):
        base_cache_test(self, "move-damage-class", '011')

    def test_get_move_learn_method_011(self):
        base_cache_test(self, "move-learn-method", '011')

    def test_get_move_target_011(self):
        base_cache_test(self, "move-target", '011')

    def test_get_location_011(self):
        base_cache_test(self, "location", '011')

    def test_get_location_area_011(self):
        base_cache_test(self, "location-area", '011')

    def test_get_pal_park_area_011(self):
        base_cache_test(self, "pal-park-area", '011')

    def test_get_region_011(self):
        base_cache_test(self, "region", '011')

    def test_get_ability_011(self):
        base_cache_test(self, "ability", '011')

    def test_get_characteristic_011(self):
        base_cache_test(self, "characteristic", '011')

    def test_get_egg_group_011(self):
        base_cache_test(self, "egg-group", '011')

    def test_get_gender_011(self):
        base_cache_test(self, "gender", '011')

    def test_get_growth_rate_011(self):
        base_cache_test(self, "growth-rate", '011')

    def test_get_nature_011(self):
        base_cache_test(self, "nature", '011')

    def test_get_pokeathlon_stat_011(self):
        base_cache_test(self, "pokeathlon-stat", '011')

    def test_get_pokemon_011(self):
        base_cache_test(self, "pokemon", '011')

    def test_get_pokemon_color_011(self):
        base_cache_test(self, "pokemon-color", '011')

    def test_get_pokemon_form_011(self):
        base_cache_test(self, "pokemon-form", '011')

    def test_get_pokemon_habitat_011(self):
        base_cache_test(self, "pokemon-habitat", '011')

    def test_get_pokemon_shape_011(self):
        base_cache_test(self, "pokemon-shape", '011')

    def test_get_pokemon_species_011(self):
        base_cache_test(self, "pokemon-species", '011')

    def test_get_stat_011(self):
        base_cache_test(self, "stat", '011')

    def test_get_type_011(self):
        base_cache_test(self, "type", '011')

    def test_get_language_011(self):
        base_cache_test(self, "language", '011')

    # 111 - 1 hit, 1 miss, 1 cached

    def test_get_berry_111(self):
        base_cache_test(self, "berry", '111')

    def test_get_berry_firmness_111(self):
        base_cache_test(self, "berry-firmness", '111')

    def test_get_berry_flavor_111(self):
        base_cache_test(self, "berry-flavor", '111')

    def test_get_contest_type_111(self):
        base_cache_test(self, "contest-type", '111')

    def test_get_contest_effect_111(self):
        base_cache_test(self, "contest-effect", '111')

    def test_get_super_contest_effect_111(self):
        base_cache_test(self, "super-contest-effect", '111')

    def test_get_encounter_method_111(self):
        base_cache_test(self, "encounter-method", '111')

    def test_get_encounter_condition_111(self):
        base_cache_test(self, "encounter-condition", '111')

    def test_get_encounter_condition_value_111(self):
        base_cache_test(self, "encounter-condition-value", '111')

    def test_get_evolution_chain_111(self):
        base_cache_test(self, "evolution-chain", '111')

    def test_get_evolution_trigger_111(self):
        base_cache_test(self, "evolution-trigger", '111')

    def test_get_generation_111(self):
        base_cache_test(self, "generation", '111')

    def test_get_pokedex_111(self):
        base_cache_test(self, "pokedex", '111')

    def test_get_version_111(self):
        base_cache_test(self, "version", '111')

    def test_get_version_group_111(self):
        base_cache_test(self, "version-group", '111')

    def test_get_item_111(self):
        base_cache_test(self, "item", '111')

    def test_get_item_attribute_111(self):
        base_cache_test(self, "item-attribute", '111')

    def test_get_item_category_111(self):
        base_cache_test(self, "item-category", '111')

    def test_get_item_fling_effect_111(self):
        base_cache_test(self, "item-fling-effect", '111')

    def test_get_item_pocket_111(self):
        base_cache_test(self, "item-pocket", '111')

    def test_get_machine_111(self):
        base_cache_test(self, "machine", '111')

    def test_get_move_111(self):
        base_cache_test(self, "move", '111')

    def test_get_move_ailment_111(self):
        base_cache_test(self, "move-ailment", '111')

    def test_get_move_battle_style_111(self):
        base_cache_test(self, "move-battle-style", '111')

    def test_get_move_category_111(self):
        base_cache_test(self, "move-category", '111')

    def test_get_move_damage_class_111(self):
        base_cache_test(self, "move-damage-class", '111')

    def test_get_move_learn_method_111(self):
        base_cache_test(self, "move-learn-method", '111')

    def test_get_move_target_111(self):
        base_cache_test(self, "move-target", '111')

    def test_get_location_111(self):
        base_cache_test(self, "location", '111')

    def test_get_location_area_111(self):
        base_cache_test(self, "location-area", '111')

    def test_get_pal_park_area_111(self):
        base_cache_test(self, "pal-park-area", '111')

    def test_get_region_111(self):
        base_cache_test(self, "region", '111')

    def test_get_ability_111(self):
        base_cache_test(self, "ability", '111')

    def test_get_characteristic_111(self):
        base_cache_test(self, "characteristic", '111')

    def test_get_egg_group_111(self):
        base_cache_test(self, "egg-group", '111')

    def test_get_gender_111(self):
        base_cache_test(self, "gender", '111')

    def test_get_growth_rate_111(self):
        base_cache_test(self, "growth-rate", '111')

    def test_get_nature_111(self):
        base_cache_test(self, "nature", '111')

    def test_get_pokeathlon_stat_111(self):
        base_cache_test(self, "pokeathlon-stat", '111')

    def test_get_pokemon_111(self):
        base_cache_test(self, "pokemon", '111')

    def test_get_pokemon_color_111(self):
        base_cache_test(self, "pokemon-color", '111')

    def test_get_pokemon_form_111(self):
        base_cache_test(self, "pokemon-form", '111')

    def test_get_pokemon_habitat_111(self):
        base_cache_test(self, "pokemon-habitat", '111')

    def test_get_pokemon_shape_111(self):
        base_cache_test(self, "pokemon-shape", '111')

    def test_get_pokemon_species_111(self):
        base_cache_test(self, "pokemon-species", '111')

    def test_get_stat_111(self):
        base_cache_test(self, "stat", '111')

    def test_get_type_111(self):
        base_cache_test(self, "type", '111')

    def test_get_language_111(self):
        base_cache_test(self, "language", '111')

    # 022 - 0 hit, 2 miss, 2 cached

    def test_get_berry_022(self):
        base_cache_test(self, "berry", '022')

    def test_get_berry_firmness_022(self):
        base_cache_test(self, "berry-firmness", '022')

    def test_get_berry_flavor_022(self):
        base_cache_test(self, "berry-flavor", '022')

    def test_get_contest_type_022(self):
        base_cache_test(self, "contest-type", '022')

    def test_get_contest_effect_022(self):
        base_cache_test(self, "contest-effect", '022')

    def test_get_super_contest_effect_022(self):
        base_cache_test(self, "super-contest-effect", '022')

    def test_get_encounter_method_022(self):
        base_cache_test(self, "encounter-method", '022')

    def test_get_encounter_condition_022(self):
        base_cache_test(self, "encounter-condition", '022')

    def test_get_encounter_condition_value_022(self):
        base_cache_test(self, "encounter-condition-value", '022')

    def test_get_evolution_chain_022(self):
        base_cache_test(self, "evolution-chain", '022')

    def test_get_evolution_trigger_022(self):
        base_cache_test(self, "evolution-trigger", '022')

    def test_get_generation_022(self):
        base_cache_test(self, "generation", '022')

    def test_get_pokedex_022(self):
        base_cache_test(self, "pokedex", '022')

    def test_get_version_022(self):
        base_cache_test(self, "version", '022')

    def test_get_version_group_022(self):
        base_cache_test(self, "version-group", '022')

    def test_get_item_022(self):
        base_cache_test(self, "item", '022')

    def test_get_item_attribute_022(self):
        base_cache_test(self, "item-attribute", '022')

    def test_get_item_category_022(self):
        base_cache_test(self, "item-category", '022')

    def test_get_item_fling_effect_022(self):
        base_cache_test(self, "item-fling-effect", '022')

    def test_get_item_pocket_022(self):
        base_cache_test(self, "item-pocket", '022')

    def test_get_machine_022(self):
        base_cache_test(self, "machine", '022')

    def test_get_move_022(self):
        base_cache_test(self, "move", '022')

    def test_get_move_ailment_022(self):
        base_cache_test(self, "move-ailment", '022')

    def test_get_move_battle_style_022(self):
        base_cache_test(self, "move-battle-style", '022')

    def test_get_move_category_022(self):
        base_cache_test(self, "move-category", '022')

    def test_get_move_damage_class_022(self):
        base_cache_test(self, "move-damage-class", '022')

    def test_get_move_learn_method_022(self):
        base_cache_test(self, "move-learn-method", '022')

    def test_get_move_target_022(self):
        base_cache_test(self, "move-target", '022')

    def test_get_location_022(self):
        base_cache_test(self, "location", '022')

    def test_get_location_area_022(self):
        base_cache_test(self, "location-area", '022')

    def test_get_pal_park_area_022(self):
        base_cache_test(self, "pal-park-area", '022')

    def test_get_region_022(self):
        base_cache_test(self, "region", '022')

    def test_get_ability_022(self):
        base_cache_test(self, "ability", '022')

    def test_get_characteristic_022(self):
        base_cache_test(self, "characteristic", '022')

    def test_get_egg_group_022(self):
        base_cache_test(self, "egg-group", '022')

    def test_get_gender_022(self):
        base_cache_test(self, "gender", '022')

    def test_get_growth_rate_022(self):
        base_cache_test(self, "growth-rate", '022')

    def test_get_nature_022(self):
        base_cache_test(self, "nature", '022')

    def test_get_pokeathlon_stat_022(self):
        base_cache_test(self, "pokeathlon-stat", '022')

    def test_get_pokemon_022(self):
        base_cache_test(self, "pokemon", '022')

    def test_get_pokemon_color_022(self):
        base_cache_test(self, "pokemon-color", '022')

    def test_get_pokemon_form_022(self):
        base_cache_test(self, "pokemon-form", '022')

    def test_get_pokemon_habitat_022(self):
        base_cache_test(self, "pokemon-habitat", '022')

    def test_get_pokemon_shape_022(self):
        base_cache_test(self, "pokemon-shape", '022')

    def test_get_pokemon_species_022(self):
        base_cache_test(self, "pokemon-species", '022')

    def test_get_stat_022(self):
        base_cache_test(self, "stat", '022')

    def test_get_type_022(self):
        base_cache_test(self, "type", '022')

    def test_get_language_022(self):
        base_cache_test(self, "language", '022')


class TestV2ClientCacheInDisk(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = pokepy.V2Client(cache='in_disk')  # cache_location=None (default)

    @classmethod
    def tearDownClass(cls):
        # remove V2Client to avoid problems with cache directory being locked
        del cls.client

        # remove cache directory
        cache_directory = appdirs.user_cache_dir('pokepy')  # same as defined in caching.memoize
        shutil.rmtree(cache_directory)

    def test_cache_type(self):
        self.assertEqual(self.client.cache_type, 'in_disk')

    # cache_info

    def test_get_berry_cache_info(self):
        base_cache_test(self, 'berry', 'cache_info')

    def test_get_berry_firmness_cache_info(self):
        base_cache_test(self, 'berry-firmness', 'cache_info')

    def test_get_berry_flavor_cache_info(self):
        base_cache_test(self, 'berry-flavor', 'cache_info')

    def test_get_contest_type_cache_info(self):
        base_cache_test(self, 'contest-type', 'cache_info')

    def test_get_contest_effect_cache_info(self):
        base_cache_test(self, 'contest-effect', 'cache_info')

    def test_get_super_contest_effect_cache_info(self):
        base_cache_test(self, 'super-contest-effect', 'cache_info')

    def test_get_encounter_method_cache_info(self):
        base_cache_test(self, 'encounter-method', 'cache_info')

    def test_get_encounter_condition_cache_info(self):
        base_cache_test(self, 'encounter-condition', 'cache_info')

    def test_get_encounter_condition_value_cache_info(self):
        base_cache_test(self, 'encounter-condition-value', 'cache_info')

    def test_get_evolution_chain_cache_info(self):
        base_cache_test(self, 'evolution-chain', 'cache_info')

    def test_get_evolution_trigger_cache_info(self):
        base_cache_test(self, 'evolution-trigger', 'cache_info')

    def test_get_generation_cache_info(self):
        base_cache_test(self, 'generation', 'cache_info')

    def test_get_pokedex_cache_info(self):
        base_cache_test(self, 'pokedex', 'cache_info')

    def test_get_version_cache_info(self):
        base_cache_test(self, 'version', 'cache_info')

    def test_get_version_group_cache_info(self):
        base_cache_test(self, 'version-group', 'cache_info')

    def test_get_item_cache_info(self):
        base_cache_test(self, 'item', 'cache_info')

    def test_get_item_attribute_cache_info(self):
        base_cache_test(self, 'item-attribute', 'cache_info')

    def test_get_item_category_cache_info(self):
        base_cache_test(self, 'item-category', 'cache_info')

    def test_get_item_fling_effect_cache_info(self):
        base_cache_test(self, 'item-fling-effect', 'cache_info')

    def test_get_item_pocket_cache_info(self):
        base_cache_test(self, 'item-pocket', 'cache_info')

    def test_get_machine_cache_info(self):
        base_cache_test(self, 'machine', 'cache_info')

    def test_get_move_cache_info(self):
        base_cache_test(self, 'move', 'cache_info')

    def test_get_move_ailment_cache_info(self):
        base_cache_test(self, 'move-ailment', 'cache_info')

    def test_get_move_battle_style_cache_info(self):
        base_cache_test(self, 'move-battle-style', 'cache_info')

    def test_get_move_category_cache_info(self):
        base_cache_test(self, 'move-category', 'cache_info')

    def test_get_move_damage_class_cache_info(self):
        base_cache_test(self, 'move-damage-class', 'cache_info')

    def test_get_move_learn_method_cache_info(self):
        base_cache_test(self, 'move-learn-method', 'cache_info')

    def test_get_move_target_cache_info(self):
        base_cache_test(self, 'move-target', 'cache_info')

    def test_get_location_cache_info(self):
        base_cache_test(self, 'location', 'cache_info')

    def test_get_location_area_cache_info(self):
        base_cache_test(self, 'location-area', 'cache_info')

    def test_get_pal_park_area_cache_info(self):
        base_cache_test(self, 'pal-park-area', 'cache_info')

    def test_get_region_cache_info(self):
        base_cache_test(self, 'region', 'cache_info')

    def test_get_ability_cache_info(self):
        base_cache_test(self, 'ability', 'cache_info')

    def test_get_characteristic_cache_info(self):
        base_cache_test(self, 'characteristic', 'cache_info')

    def test_get_egg_group_cache_info(self):
        base_cache_test(self, 'egg-group', 'cache_info')

    def test_get_gender_cache_info(self):
        base_cache_test(self, 'gender', 'cache_info')

    def test_get_growth_rate_cache_info(self):
        base_cache_test(self, 'growth-rate', 'cache_info')

    def test_get_nature_cache_info(self):
        base_cache_test(self, 'nature', 'cache_info')

    def test_get_pokeathlon_stat_cache_info(self):
        base_cache_test(self, 'pokeathlon-stat', 'cache_info')

    def test_get_pokemon_cache_info(self):
        base_cache_test(self, 'pokemon', 'cache_info')

    def test_get_pokemon_color_cache_info(self):
        base_cache_test(self, 'pokemon-color', 'cache_info')

    def test_get_pokemon_form_cache_info(self):
        base_cache_test(self, 'pokemon-form', 'cache_info')

    def test_get_pokemon_habitat_cache_info(self):
        base_cache_test(self, 'pokemon-habitat', 'cache_info')

    def test_get_pokemon_shape_cache_info(self):
        base_cache_test(self, 'pokemon-shape', 'cache_info')

    def test_get_pokemon_species_cache_info(self):
        base_cache_test(self, 'pokemon-species', 'cache_info')

    def test_get_stat_cache_info(self):
        base_cache_test(self, 'stat', 'cache_info')

    def test_get_type_cache_info(self):
        base_cache_test(self, 'type', 'cache_info')

    def test_get_language_cache_info(self):
        base_cache_test(self, 'language', 'cache_info')

    # cache_clear

    def test_get_berry_cache_clear(self):
        base_cache_test(self, "berry", 'cache_clear')

    def test_get_berry_firmness_cache_clear(self):
        base_cache_test(self, "berry-firmness", 'cache_clear')

    def test_get_berry_flavor_cache_clear(self):
        base_cache_test(self, "berry-flavor", 'cache_clear')

    def test_get_contest_type_cache_clear(self):
        base_cache_test(self, "contest-type", 'cache_clear')

    def test_get_contest_effect_cache_clear(self):
        base_cache_test(self, "contest-effect", 'cache_clear')

    def test_get_super_contest_effect_cache_clear(self):
        base_cache_test(self, "super-contest-effect", 'cache_clear')

    def test_get_encounter_method_cache_clear(self):
        base_cache_test(self, "encounter-method", 'cache_clear')

    def test_get_encounter_condition_cache_clear(self):
        base_cache_test(self, "encounter-condition", 'cache_clear')

    def test_get_encounter_condition_value_cache_clear(self):
        base_cache_test(self, "encounter-condition-value", 'cache_clear')

    def test_get_evolution_chain_cache_clear(self):
        base_cache_test(self, "evolution-chain", 'cache_clear')

    def test_get_evolution_trigger_cache_clear(self):
        base_cache_test(self, "evolution-trigger", 'cache_clear')

    def test_get_generation_cache_clear(self):
        base_cache_test(self, "generation", 'cache_clear')

    def test_get_pokedex_cache_clear(self):
        base_cache_test(self, "pokedex", 'cache_clear')

    def test_get_version_cache_clear(self):
        base_cache_test(self, "version", 'cache_clear')

    def test_get_version_group_cache_clear(self):
        base_cache_test(self, "version-group", 'cache_clear')

    def test_get_item_cache_clear(self):
        base_cache_test(self, "item", 'cache_clear')

    def test_get_item_attribute_cache_clear(self):
        base_cache_test(self, "item-attribute", 'cache_clear')

    def test_get_item_category_cache_clear(self):
        base_cache_test(self, "item-category", 'cache_clear')

    def test_get_item_fling_effect_cache_clear(self):
        base_cache_test(self, "item-fling-effect", 'cache_clear')

    def test_get_item_pocket_cache_clear(self):
        base_cache_test(self, "item-pocket", 'cache_clear')

    def test_get_machine_cache_clear(self):
        base_cache_test(self, "machine", 'cache_clear')

    def test_get_move_cache_clear(self):
        base_cache_test(self, "move", 'cache_clear')

    def test_get_move_ailment_cache_clear(self):
        base_cache_test(self, "move-ailment", 'cache_clear')

    def test_get_move_battle_style_cache_clear(self):
        base_cache_test(self, "move-battle-style", 'cache_clear')

    def test_get_move_category_cache_clear(self):
        base_cache_test(self, "move-category", 'cache_clear')

    def test_get_move_damage_class_cache_clear(self):
        base_cache_test(self, "move-damage-class", 'cache_clear')

    def test_get_move_learn_method_cache_clear(self):
        base_cache_test(self, "move-learn-method", 'cache_clear')

    def test_get_move_target_cache_clear(self):
        base_cache_test(self, "move-target", 'cache_clear')

    def test_get_location_cache_clear(self):
        base_cache_test(self, "location", 'cache_clear')

    def test_get_location_area_cache_clear(self):
        base_cache_test(self, "location-area", 'cache_clear')

    def test_get_pal_park_area_cache_clear(self):
        base_cache_test(self, "pal-park-area", 'cache_clear')

    def test_get_region_cache_clear(self):
        base_cache_test(self, "region", 'cache_clear')

    def test_get_ability_cache_clear(self):
        base_cache_test(self, "ability", 'cache_clear')

    def test_get_characteristic_cache_clear(self):
        base_cache_test(self, "characteristic", 'cache_clear')

    def test_get_egg_group_cache_clear(self):
        base_cache_test(self, "egg-group", 'cache_clear')

    def test_get_gender_cache_clear(self):
        base_cache_test(self, "gender", 'cache_clear')

    def test_get_growth_rate_cache_clear(self):
        base_cache_test(self, "growth-rate", 'cache_clear')

    def test_get_nature_cache_clear(self):
        base_cache_test(self, "nature", 'cache_clear')

    def test_get_pokeathlon_stat_cache_clear(self):
        base_cache_test(self, "pokeathlon-stat", 'cache_clear')

    def test_get_pokemon_cache_clear(self):
        base_cache_test(self, "pokemon", 'cache_clear')

    def test_get_pokemon_color_cache_clear(self):
        base_cache_test(self, "pokemon-color", 'cache_clear')

    def test_get_pokemon_form_cache_clear(self):
        base_cache_test(self, "pokemon-form", 'cache_clear')

    def test_get_pokemon_habitat_cache_clear(self):
        base_cache_test(self, "pokemon-habitat", 'cache_clear')

    def test_get_pokemon_shape_cache_clear(self):
        base_cache_test(self, "pokemon-shape", 'cache_clear')

    def test_get_pokemon_species_cache_clear(self):
        base_cache_test(self, "pokemon-species", 'cache_clear')

    def test_get_stat_cache_clear(self):
        base_cache_test(self, "stat", 'cache_clear')

    def test_get_type_cache_clear(self):
        base_cache_test(self, "type", 'cache_clear')

    def test_get_language_cache_clear(self):
        base_cache_test(self, "language", 'cache_clear')

    # cache_location

    def test_get_berry_cache_location(self):
        base_cache_test(self, "berry", 'cache_location')

    def test_get_berry_firmness_cache_location(self):
        base_cache_test(self, "berry-firmness", 'cache_location')

    def test_get_berry_flavor_cache_location(self):
        base_cache_test(self, "berry-flavor", 'cache_location')

    def test_get_contest_type_cache_location(self):
        base_cache_test(self, "contest-type", 'cache_location')

    def test_get_contest_effect_cache_location(self):
        base_cache_test(self, "contest-effect", 'cache_location')

    def test_get_super_contest_effect_cache_location(self):
        base_cache_test(self, "super-contest-effect", 'cache_location')

    def test_get_encounter_method_cache_location(self):
        base_cache_test(self, "encounter-method", 'cache_location')

    def test_get_encounter_condition_cache_location(self):
        base_cache_test(self, "encounter-condition", 'cache_location')

    def test_get_encounter_condition_value_cache_location(self):
        base_cache_test(self, "encounter-condition-value", 'cache_location')

    def test_get_evolution_chain_cache_location(self):
        base_cache_test(self, "evolution-chain", 'cache_location')

    def test_get_evolution_trigger_cache_location(self):
        base_cache_test(self, "evolution-trigger", 'cache_location')

    def test_get_generation_cache_location(self):
        base_cache_test(self, "generation", 'cache_location')

    def test_get_pokedex_cache_location(self):
        base_cache_test(self, "pokedex", 'cache_location')

    def test_get_version_cache_location(self):
        base_cache_test(self, "version", 'cache_location')

    def test_get_version_group_cache_location(self):
        base_cache_test(self, "version-group", 'cache_location')

    def test_get_item_cache_location(self):
        base_cache_test(self, "item", 'cache_location')

    def test_get_item_attribute_cache_location(self):
        base_cache_test(self, "item-attribute", 'cache_location')

    def test_get_item_category_cache_location(self):
        base_cache_test(self, "item-category", 'cache_location')

    def test_get_item_fling_effect_cache_location(self):
        base_cache_test(self, "item-fling-effect", 'cache_location')

    def test_get_item_pocket_cache_location(self):
        base_cache_test(self, "item-pocket", 'cache_location')

    def test_get_machine_cache_location(self):
        base_cache_test(self, "machine", 'cache_location')

    def test_get_move_cache_location(self):
        base_cache_test(self, "move", 'cache_location')

    def test_get_move_ailment_cache_location(self):
        base_cache_test(self, "move-ailment", 'cache_location')

    def test_get_move_battle_style_cache_location(self):
        base_cache_test(self, "move-battle-style", 'cache_location')

    def test_get_move_category_cache_location(self):
        base_cache_test(self, "move-category", 'cache_location')

    def test_get_move_damage_class_cache_location(self):
        base_cache_test(self, "move-damage-class", 'cache_location')

    def test_get_move_learn_method_cache_location(self):
        base_cache_test(self, "move-learn-method", 'cache_location')

    def test_get_move_target_cache_location(self):
        base_cache_test(self, "move-target", 'cache_location')

    def test_get_location_cache_location(self):
        base_cache_test(self, "location", 'cache_location')

    def test_get_location_area_cache_location(self):
        base_cache_test(self, "location-area", 'cache_location')

    def test_get_pal_park_area_cache_location(self):
        base_cache_test(self, "pal-park-area", 'cache_location')

    def test_get_region_cache_location(self):
        base_cache_test(self, "region", 'cache_location')

    def test_get_ability_cache_location(self):
        base_cache_test(self, "ability", 'cache_location')

    def test_get_characteristic_cache_location(self):
        base_cache_test(self, "characteristic", 'cache_location')

    def test_get_egg_group_cache_location(self):
        base_cache_test(self, "egg-group", 'cache_location')

    def test_get_gender_cache_location(self):
        base_cache_test(self, "gender", 'cache_location')

    def test_get_growth_rate_cache_location(self):
        base_cache_test(self, "growth-rate", 'cache_location')

    def test_get_nature_cache_location(self):
        base_cache_test(self, "nature", 'cache_location')

    def test_get_pokeathlon_stat_cache_location(self):
        base_cache_test(self, "pokeathlon-stat", 'cache_location')

    def test_get_pokemon_cache_location(self):
        base_cache_test(self, "pokemon", 'cache_location')

    def test_get_pokemon_color_cache_location(self):
        base_cache_test(self, "pokemon-color", 'cache_location')

    def test_get_pokemon_form_cache_location(self):
        base_cache_test(self, "pokemon-form", 'cache_location')

    def test_get_pokemon_habitat_cache_location(self):
        base_cache_test(self, "pokemon-habitat", 'cache_location')

    def test_get_pokemon_shape_cache_location(self):
        base_cache_test(self, "pokemon-shape", 'cache_location')

    def test_get_pokemon_species_cache_location(self):
        base_cache_test(self, "pokemon-species", 'cache_location')

    def test_get_stat_cache_location(self):
        base_cache_test(self, "stat", 'cache_location')

    def test_get_type_cache_location(self):
        base_cache_test(self, "type", 'cache_location')

    def test_get_language_cache_location(self):
        base_cache_test(self, "language", 'cache_location')

    # 011 - 0 hit, 1 miss, 1 cached

    def test_get_berry_011(self):
        base_cache_test(self, "berry", '011')

    def test_get_berry_firmness_011(self):
        base_cache_test(self, "berry-firmness", '011')

    def test_get_berry_flavor_011(self):
        base_cache_test(self, "berry-flavor", '011')

    def test_get_contest_type_011(self):
        base_cache_test(self, "contest-type", '011')

    def test_get_contest_effect_011(self):
        base_cache_test(self, "contest-effect", '011')

    def test_get_super_contest_effect_011(self):
        base_cache_test(self, "super-contest-effect", '011')

    def test_get_encounter_method_011(self):
        base_cache_test(self, "encounter-method", '011')

    def test_get_encounter_condition_011(self):
        base_cache_test(self, "encounter-condition", '011')

    def test_get_encounter_condition_value_011(self):
        base_cache_test(self, "encounter-condition-value", '011')

    def test_get_evolution_chain_011(self):
        base_cache_test(self, "evolution-chain", '011')

    def test_get_evolution_trigger_011(self):
        base_cache_test(self, "evolution-trigger", '011')

    def test_get_generation_011(self):
        base_cache_test(self, "generation", '011')

    def test_get_pokedex_011(self):
        base_cache_test(self, "pokedex", '011')

    def test_get_version_011(self):
        base_cache_test(self, "version", '011')

    def test_get_version_group_011(self):
        base_cache_test(self, "version-group", '011')

    def test_get_item_011(self):
        base_cache_test(self, "item", '011')

    def test_get_item_attribute_011(self):
        base_cache_test(self, "item-attribute", '011')

    def test_get_item_category_011(self):
        base_cache_test(self, "item-category", '011')

    def test_get_item_fling_effect_011(self):
        base_cache_test(self, "item-fling-effect", '011')

    def test_get_item_pocket_011(self):
        base_cache_test(self, "item-pocket", '011')

    def test_get_machine_011(self):
        base_cache_test(self, "machine", '011')

    def test_get_move_011(self):
        base_cache_test(self, "move", '011')

    def test_get_move_ailment_011(self):
        base_cache_test(self, "move-ailment", '011')

    def test_get_move_battle_style_011(self):
        base_cache_test(self, "move-battle-style", '011')

    def test_get_move_category_011(self):
        base_cache_test(self, "move-category", '011')

    def test_get_move_damage_class_011(self):
        base_cache_test(self, "move-damage-class", '011')

    def test_get_move_learn_method_011(self):
        base_cache_test(self, "move-learn-method", '011')

    def test_get_move_target_011(self):
        base_cache_test(self, "move-target", '011')

    def test_get_location_011(self):
        base_cache_test(self, "location", '011')

    def test_get_location_area_011(self):
        base_cache_test(self, "location-area", '011')

    def test_get_pal_park_area_011(self):
        base_cache_test(self, "pal-park-area", '011')

    def test_get_region_011(self):
        base_cache_test(self, "region", '011')

    def test_get_ability_011(self):
        base_cache_test(self, "ability", '011')

    def test_get_characteristic_011(self):
        base_cache_test(self, "characteristic", '011')

    def test_get_egg_group_011(self):
        base_cache_test(self, "egg-group", '011')

    def test_get_gender_011(self):
        base_cache_test(self, "gender", '011')

    def test_get_growth_rate_011(self):
        base_cache_test(self, "growth-rate", '011')

    def test_get_nature_011(self):
        base_cache_test(self, "nature", '011')

    def test_get_pokeathlon_stat_011(self):
        base_cache_test(self, "pokeathlon-stat", '011')

    def test_get_pokemon_011(self):
        base_cache_test(self, "pokemon", '011')

    def test_get_pokemon_color_011(self):
        base_cache_test(self, "pokemon-color", '011')

    def test_get_pokemon_form_011(self):
        base_cache_test(self, "pokemon-form", '011')

    def test_get_pokemon_habitat_011(self):
        base_cache_test(self, "pokemon-habitat", '011')

    def test_get_pokemon_shape_011(self):
        base_cache_test(self, "pokemon-shape", '011')

    def test_get_pokemon_species_011(self):
        base_cache_test(self, "pokemon-species", '011')

    def test_get_stat_011(self):
        base_cache_test(self, "stat", '011')

    def test_get_type_011(self):
        base_cache_test(self, "type", '011')

    def test_get_language_011(self):
        base_cache_test(self, "language", '011')

    # 111 - 1 hit, 1 miss, 1 cached

    def test_get_berry_111(self):
        base_cache_test(self, "berry", '111')

    def test_get_berry_firmness_111(self):
        base_cache_test(self, "berry-firmness", '111')

    def test_get_berry_flavor_111(self):
        base_cache_test(self, "berry-flavor", '111')

    def test_get_contest_type_111(self):
        base_cache_test(self, "contest-type", '111')

    def test_get_contest_effect_111(self):
        base_cache_test(self, "contest-effect", '111')

    def test_get_super_contest_effect_111(self):
        base_cache_test(self, "super-contest-effect", '111')

    def test_get_encounter_method_111(self):
        base_cache_test(self, "encounter-method", '111')

    def test_get_encounter_condition_111(self):
        base_cache_test(self, "encounter-condition", '111')

    def test_get_encounter_condition_value_111(self):
        base_cache_test(self, "encounter-condition-value", '111')

    def test_get_evolution_chain_111(self):
        base_cache_test(self, "evolution-chain", '111')

    def test_get_evolution_trigger_111(self):
        base_cache_test(self, "evolution-trigger", '111')

    def test_get_generation_111(self):
        base_cache_test(self, "generation", '111')

    def test_get_pokedex_111(self):
        base_cache_test(self, "pokedex", '111')

    def test_get_version_111(self):
        base_cache_test(self, "version", '111')

    def test_get_version_group_111(self):
        base_cache_test(self, "version-group", '111')

    def test_get_item_111(self):
        base_cache_test(self, "item", '111')

    def test_get_item_attribute_111(self):
        base_cache_test(self, "item-attribute", '111')

    def test_get_item_category_111(self):
        base_cache_test(self, "item-category", '111')

    def test_get_item_fling_effect_111(self):
        base_cache_test(self, "item-fling-effect", '111')

    def test_get_item_pocket_111(self):
        base_cache_test(self, "item-pocket", '111')

    def test_get_machine_111(self):
        base_cache_test(self, "machine", '111')

    def test_get_move_111(self):
        base_cache_test(self, "move", '111')

    def test_get_move_ailment_111(self):
        base_cache_test(self, "move-ailment", '111')

    def test_get_move_battle_style_111(self):
        base_cache_test(self, "move-battle-style", '111')

    def test_get_move_category_111(self):
        base_cache_test(self, "move-category", '111')

    def test_get_move_damage_class_111(self):
        base_cache_test(self, "move-damage-class", '111')

    def test_get_move_learn_method_111(self):
        base_cache_test(self, "move-learn-method", '111')

    def test_get_move_target_111(self):
        base_cache_test(self, "move-target", '111')

    def test_get_location_111(self):
        base_cache_test(self, "location", '111')

    def test_get_location_area_111(self):
        base_cache_test(self, "location-area", '111')

    def test_get_pal_park_area_111(self):
        base_cache_test(self, "pal-park-area", '111')

    def test_get_region_111(self):
        base_cache_test(self, "region", '111')

    def test_get_ability_111(self):
        base_cache_test(self, "ability", '111')

    def test_get_characteristic_111(self):
        base_cache_test(self, "characteristic", '111')

    def test_get_egg_group_111(self):
        base_cache_test(self, "egg-group", '111')

    def test_get_gender_111(self):
        base_cache_test(self, "gender", '111')

    def test_get_growth_rate_111(self):
        base_cache_test(self, "growth-rate", '111')

    def test_get_nature_111(self):
        base_cache_test(self, "nature", '111')

    def test_get_pokeathlon_stat_111(self):
        base_cache_test(self, "pokeathlon-stat", '111')

    def test_get_pokemon_111(self):
        base_cache_test(self, "pokemon", '111')

    def test_get_pokemon_color_111(self):
        base_cache_test(self, "pokemon-color", '111')

    def test_get_pokemon_form_111(self):
        base_cache_test(self, "pokemon-form", '111')

    def test_get_pokemon_habitat_111(self):
        base_cache_test(self, "pokemon-habitat", '111')

    def test_get_pokemon_shape_111(self):
        base_cache_test(self, "pokemon-shape", '111')

    def test_get_pokemon_species_111(self):
        base_cache_test(self, "pokemon-species", '111')

    def test_get_stat_111(self):
        base_cache_test(self, "stat", '111')

    def test_get_type_111(self):
        base_cache_test(self, "type", '111')

    def test_get_language_111(self):
        base_cache_test(self, "language", '111')

    # 022 - 0 hit, 2 miss, 2 cached

    def test_get_berry_022(self):
        base_cache_test(self, "berry", '022')

    def test_get_berry_firmness_022(self):
        base_cache_test(self, "berry-firmness", '022')

    def test_get_berry_flavor_022(self):
        base_cache_test(self, "berry-flavor", '022')

    def test_get_contest_type_022(self):
        base_cache_test(self, "contest-type", '022')

    def test_get_contest_effect_022(self):
        base_cache_test(self, "contest-effect", '022')

    def test_get_super_contest_effect_022(self):
        base_cache_test(self, "super-contest-effect", '022')

    def test_get_encounter_method_022(self):
        base_cache_test(self, "encounter-method", '022')

    def test_get_encounter_condition_022(self):
        base_cache_test(self, "encounter-condition", '022')

    def test_get_encounter_condition_value_022(self):
        base_cache_test(self, "encounter-condition-value", '022')

    def test_get_evolution_chain_022(self):
        base_cache_test(self, "evolution-chain", '022')

    def test_get_evolution_trigger_022(self):
        base_cache_test(self, "evolution-trigger", '022')

    def test_get_generation_022(self):
        base_cache_test(self, "generation", '022')

    def test_get_pokedex_022(self):
        base_cache_test(self, "pokedex", '022')

    def test_get_version_022(self):
        base_cache_test(self, "version", '022')

    def test_get_version_group_022(self):
        base_cache_test(self, "version-group", '022')

    def test_get_item_022(self):
        base_cache_test(self, "item", '022')

    def test_get_item_attribute_022(self):
        base_cache_test(self, "item-attribute", '022')

    def test_get_item_category_022(self):
        base_cache_test(self, "item-category", '022')

    def test_get_item_fling_effect_022(self):
        base_cache_test(self, "item-fling-effect", '022')

    def test_get_item_pocket_022(self):
        base_cache_test(self, "item-pocket", '022')

    def test_get_machine_022(self):
        base_cache_test(self, "machine", '022')

    def test_get_move_022(self):
        base_cache_test(self, "move", '022')

    def test_get_move_ailment_022(self):
        base_cache_test(self, "move-ailment", '022')

    def test_get_move_battle_style_022(self):
        base_cache_test(self, "move-battle-style", '022')

    def test_get_move_category_022(self):
        base_cache_test(self, "move-category", '022')

    def test_get_move_damage_class_022(self):
        base_cache_test(self, "move-damage-class", '022')

    def test_get_move_learn_method_022(self):
        base_cache_test(self, "move-learn-method", '022')

    def test_get_move_target_022(self):
        base_cache_test(self, "move-target", '022')

    def test_get_location_022(self):
        base_cache_test(self, "location", '022')

    def test_get_location_area_022(self):
        base_cache_test(self, "location-area", '022')

    def test_get_pal_park_area_022(self):
        base_cache_test(self, "pal-park-area", '022')

    def test_get_region_022(self):
        base_cache_test(self, "region", '022')

    def test_get_ability_022(self):
        base_cache_test(self, "ability", '022')

    def test_get_characteristic_022(self):
        base_cache_test(self, "characteristic", '022')

    def test_get_egg_group_022(self):
        base_cache_test(self, "egg-group", '022')

    def test_get_gender_022(self):
        base_cache_test(self, "gender", '022')

    def test_get_growth_rate_022(self):
        base_cache_test(self, "growth-rate", '022')

    def test_get_nature_022(self):
        base_cache_test(self, "nature", '022')

    def test_get_pokeathlon_stat_022(self):
        base_cache_test(self, "pokeathlon-stat", '022')

    def test_get_pokemon_022(self):
        base_cache_test(self, "pokemon", '022')

    def test_get_pokemon_color_022(self):
        base_cache_test(self, "pokemon-color", '022')

    def test_get_pokemon_form_022(self):
        base_cache_test(self, "pokemon-form", '022')

    def test_get_pokemon_habitat_022(self):
        base_cache_test(self, "pokemon-habitat", '022')

    def test_get_pokemon_shape_022(self):
        base_cache_test(self, "pokemon-shape", '022')

    def test_get_pokemon_species_022(self):
        base_cache_test(self, "pokemon-species", '022')

    def test_get_stat_022(self):
        base_cache_test(self, "stat", '022')

    def test_get_type_022(self):
        base_cache_test(self, "type", '022')

    def test_get_language_022(self):
        base_cache_test(self, "language", '022')


if __name__ == '__main__':
    unittest.main()
