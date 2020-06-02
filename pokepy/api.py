#!/usr/bin/env python
# coding: utf-8

"""
pokepy.api

User interaction with this package is done through this file.
"""

import functools
import os
import sys
import types
from collections import namedtuple
import appdirs  # dependency of FileCache
from beckett.clients import BaseClient
from beckett.constants import DEFAULT_VALID_STATUS_CODES
from .fcache.cache import FileCache
from . import resources_v2 as rv2
from . import __version__


class V2Client(BaseClient):
    """Pokéapi client"""

    class Meta(BaseClient.Meta):
        name = 'pokepy-v2-client-' + __version__
        base_url = 'https://pokeapi.co/api/v2'
        resources = (
            rv2.BerryResource,
            rv2.BerryFirmnessResource,
            rv2.BerryFlavorResource,
            rv2.ContestTypeResource,
            rv2.ContestEffectResource,
            rv2.SuperContestEffectResource,
            rv2.EncounterMethodResource,
            rv2.EncounterConditionResource,
            rv2.EncounterConditionValueResource,
            rv2.EvolutionChainResource,
            rv2.EvolutionTriggerResource,
            rv2.GenerationResource,
            rv2.PokedexResource,
            rv2.VersionResource,
            rv2.VersionGroupResource,
            rv2.ItemResource,
            rv2.ItemAttributeResource,
            rv2.ItemCategoryResource,
            rv2.ItemFlingEffectResource,
            rv2.ItemPocketResource,
            rv2.MachineResource,
            rv2.MoveResource,
            rv2.MoveAilmentResource,
            rv2.MoveBattleStyleResource,
            rv2.MoveCategoryResource,
            rv2.MoveDamageClassResource,
            rv2.MoveLearnMethodResource,
            rv2.MoveTargetResource,
            rv2.LocationResource,
            rv2.LocationAreaResource,
            rv2.PalParkAreaResource,
            rv2.RegionResource,
            rv2.AbilityResource,
            rv2.CharacteristicResource,
            rv2.EggGroupResource,
            rv2.GenderResource,
            rv2.GrowthRateResource,
            rv2.NatureResource,
            rv2.PokeathlonStatResource,
            rv2.PokemonResource,
            rv2.PokemonColorResource,
            rv2.PokemonFormResource,
            rv2.PokemonHabitatResource,
            rv2.PokemonShapeResource,
            rv2.PokemonSpeciesResource,
            rv2.StatResource,
            rv2.TypeResource,
            rv2.LanguageResource
        )

    def __init__(self, cache=None, cache_location=None, *args, **kwargs):
        """
        Parameters
        ----------
        cache: str
            cache can be 'in_memory' or 'in_disk',
            for memory-based or disk-based cache, respectively.
            Optional.
        cache_location: str
            cache directory, for disk-based cache.
            Optional.
        """
        if cache is None:  # empty wrapping function
            def no_cache(func):
                @functools.wraps(func)
                def inner(*args, **kwargs):
                    return func(*args, **kwargs)
                return inner
            cache_function = no_cache
        else:
            if cache in ['in_memory', 'in_disk']:
                cache_function = self._caching(cache.split('in_')[1], cache_location)
                self.cache_type = cache

                def cache_info_total(self):
                    return self._cache_info_(self._cache_hits_global,
                                             self._cache_misses_global,
                                             self._cache_len_global)

                def cache_clear_total(self):
                    for get_method_name in self._all_get_methods_names:
                        getattr(self, get_method_name).cache_clear()

                def cache_location_absolute(self):
                    return self._cache_location_global

                # global cache related methods
                self.cache_info = types.MethodType(cache_info_total, self)
                self.cache_clear = types.MethodType(cache_clear_total, self)
                self.cache_location = types.MethodType(cache_location_absolute, self)

                self._cache_hits_global = 0
                self._cache_misses_global = 0
                self._cache_len_global = 0
                self._cache_location_global = ''
                self._cache_info_ = namedtuple('CacheInfo', ['hits', 'misses', 'size'])
            else:  # wrong cache parameter
                raise ValueError('Accepted values for cache are "in_memory" or "in_disk"')

        self._cache = cache_function
        self._all_get_methods_names = []
        super(V2Client, self).__init__(*args, **kwargs)

    def _assign_method(self, resource_class, method_type):
        """
        Exactly the same code as the original except:
        - uid is now first parameter (after self). Therefore, no need to explicitly call 'uid='
        - Ignored the other http methods besides GET (as they are not needed for the pokeapi.co API)
        - Added cache wrapping function
        - Added a way to list all get methods
        - Added a filter for single element lists (extract element into a standalone object)
        """
        method_name = resource_class.get_method_name(
            resource_class, method_type)
        valid_status_codes = getattr(
            resource_class.Meta,
            'valid_status_codes',
            DEFAULT_VALID_STATUS_CODES
        )

        def extract_single_element_list(func):
            @functools.wraps(func)
            def inner(*args, **kwargs):
                final = func(*args, **kwargs)
                if len(final) == 1:
                    final = final[0]
                return final
            return inner

        # uid is now the first argument (after self)
        @self._cache
        @extract_single_element_list
        def get(self, uid=None, method_type=method_type,
                method_name=method_name,
                valid_status_codes=valid_status_codes,
                resource=resource_class, data=None, **kwargs):
            uid = uid.lower() if isinstance(uid, str) else uid
            return self.call_api(
                method_type, method_name,
                valid_status_codes, resource,
                data, uid=uid, **kwargs)

        # only GET method is used
        setattr(
            self, method_name,
            types.MethodType(get, self)
        )

        # for easier listing of get methods
        self._all_get_methods_names.append(method_name)

    def _caching(self, disk_or_memory, cache_directory=None):
        """
        Decorator that allows caching the outputs of the BaseClient get methods.
        Cache can be either disk- or memory-based.
        Disk-based cache is reloaded automatically between runs if the same
        cache directory is specified.
        Cache is kept per each unique uid.

        ex:
        >> client.get_pokemon(1)        ->  output gets cached
        >> client.get_pokemon(uid=1)    ->  output already cached
        >> client.get_pokemon(2)        ->  output gets cached

        Parameters
        ----------
        disk_or_memory: str
            Specify if the cache is disk- or memory-based. Accepts 'disk' or 'memory'.
        cache_directory: str
            Specify the directory for the disk-based cache.
            Optional, will chose an appropriate and platform-specific directory if not specified.
            Ignored if memory-based cache is selected.
        """
        if disk_or_memory not in ('disk', 'memory'):
            raise ValueError('Accepted values are "disk" or "memory"')

        # Because of how BaseClient get methods are generated, they don't get a proper __name__.
        # As such, it is hard to generate a specific cache directory name for each get method.
        # Therefore, I decided to just generate a number for each folder, starting at zero.
        # The same get methods get the same number every time because their order doesn't change.
        # Also, variable is incremented inside a list because nonlocals are only python 3.0 and up.
        get_methods_id = [0]

        def memoize(func):
            _global_cache_dir = ''

            if disk_or_memory == 'disk':
                if cache_directory:
                    # Python 2 and 3.4 workaround
                    if (sys.version_info[0] == 2 and not
                            isinstance(cache_directory, (str, unicode))) or (
                                sys.version_info[0:2] == (3, 4) and not
                                isinstance(cache_directory, str)):
                        raise TypeError('expected str, not %s' % cache_directory.__class__.__name__)

                    _global_cache_dir = os.path.join(cache_directory, 'pokepy_cache')
                    cache_dir = os.path.join(_global_cache_dir, str(get_methods_id[0]))
                else:
                    _global_cache_dir = appdirs.user_cache_dir('pokepy_cache', False,
                                                               opinion=False)
                    cache_dir = os.path.join(_global_cache_dir, str(get_methods_id[0]))

                cache = FileCache('pokepy', flag='cs', app_cache_dir=cache_dir)
                get_methods_id[0] += 1
            else:  # 'memory'
                cache = {}
                _global_cache_dir = 'ram'

            # global cache directory
            # should only be set when setting the first get method
            if not self._cache_location_global:
                self._cache_location_global = _global_cache_dir

            hits = [0]
            misses = [0]

            def cache_info():
                return self._cache_info_(hits[0], misses[0], len(cache))

            def cache_clear():
                # global cache info
                self._cache_hits_global -= hits[0]
                self._cache_misses_global -= misses[0]
                self._cache_len_global -= len(cache)
                # local cache info
                hits[0] = 0
                misses[0] = 0

                cache.clear()  # for disk-based cache, files are deleted but not the directories
                if disk_or_memory == 'disk':
                    cache.create()  # recreate cache file handles

            def cache_location():
                return 'ram' if disk_or_memory == 'memory' else cache.cache_dir

            @functools.wraps(func)
            def memoizer(*args, **kwargs):
                # arguments to the get methods can be a value or uid=value
                key = str(args[1]) if len(args) > 1 else str(kwargs.get("uid"))

                if key not in cache:
                    # local and global cache info
                    misses[0] += 1
                    self._cache_misses_global += 1
                    cache[key] = func(*args, **kwargs)
                    self._cache_len_global += 1
                else:
                    self._cache_hits_global += 1  # global cache info
                    hits[0] += 1  # local cache info
                return cache[key]

            memoizer.cache_info = cache_info
            memoizer.cache_clear = cache_clear
            memoizer.cache_location = cache_location
            return memoizer

        return memoize
