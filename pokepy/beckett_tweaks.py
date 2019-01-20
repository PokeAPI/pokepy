# coding: utf-8

"""
Tweaks to the beckett API plus other new functionality
"""

import functools
import os
import types
from collections import namedtuple
from fcache.cache import FileCache
from beckett.constants import DEFAULT_VALID_STATUS_CODES
from beckett.clients import BaseClient
from beckett.resources import BaseResource


def caching(disk_or_memory, cache_directory=None):
    """
    Decorator that allows caching the outputs of the BaseClient get methods.
    Cache can be either disk- or memory-based.
    Disk-based cache is reloaded automatically between runs if the same cache directory is specified.
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

    # Because of the way the BaseClient get methods are generated, they don't get a proper __name__.
    # As such, it is hard to generate a specific cache directory name for each get method.
    # Therefore, I decided to just generate a number for each folder, starting at zero.
    # The same get methods get the same number every time because the order of the methods doesn't change.
    get_methods_id = 0

    def memoize(func):
        if disk_or_memory == 'disk':
            nonlocal get_methods_id
            cache = FileCache('pokepy', flag='cs', app_cache_dir=os.path.join(cache_directory, str(get_methods_id)))
            get_methods_id += 1
        else:  # 'memory'
            cache = {}

        cache_info_ = namedtuple('CacheInfo', ['hits', 'misses', 'size'])
        hits = misses = 0

        def cache_info():
            return cache_info_(hits, misses, len(cache))

        def cache_clear():
            cache.clear()  # for disk-based cache, files are deleted but not the directories
            if disk_or_memory == 'disk':
                cache.create()  # recreate cache file handles
            nonlocal hits, misses
            hits = misses = 0

        def cache_location():
            return 'ram' if disk_or_memory == 'memory' else cache.cache_dir

        @functools.wraps(func)
        def memoizer(*args, **kwargs):
            # arguments to the get methods can be a value or uid=value
            key = str(args[1]) if len(args) > 1 else str(kwargs.get("uid"))

            nonlocal hits, misses
            if key not in cache:
                misses += 1
                cache[key] = func(*args, **kwargs)
            else:
                hits += 1
            return cache[key]

        memoizer.cache_info = cache_info
        memoizer.cache_clear = cache_clear
        memoizer.cache_location = cache_location
        return memoizer
    return memoize


class BaseClient(BaseClient):
    """
    Tweaks:
        - Allow resources to be called without having to specify 'uid='.
            ex:
            >> client.get_pokemon('bulbasaur')
            >> [<Pokemon - Bulbasaur>]
        - Removed all http methods except GET
        - Added memory- and disk-based cache
    """
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
        if cache == 'in_memory':
            cache_function = caching('memory')
        elif cache == 'in_disk':
            cache_function = caching('disk', cache_location)
        else:  # empty wrapping function
            def no_cache(func):
                @functools.wraps(func)
                def inner(*args, **kwargs):
                    return func(*args, **kwargs)
                return inner
            cache_function = no_cache

        self.cache = cache_function
        super(BaseClient, self).__init__(*args, **kwargs)

    def _assign_method(self, resource_class, method_type):
        """
        Exactly the same code as the original except:
        - uid is now first parameter (after self)
        - Ignored the other http methods besides GET (as they are not needed for the pokeapi.co API)
        - Added cache wrapping function
        """
        method_name = resource_class.get_method_name(
            resource_class, method_type)
        valid_status_codes = getattr(
            resource_class.Meta,
            'valid_status_codes',
            DEFAULT_VALID_STATUS_CODES
        )

        # uid is now the first argument (after self)
        @self.cache
        def get(self, uid=None, method_type=method_type,
                method_name=method_name,
                valid_status_codes=valid_status_codes,
                resource=resource_class, data=None, **kwargs):
            return self.call_api(
                method_type, method_name,
                valid_status_codes, resource,
                data, uid=uid, **kwargs)

        # only GET method is used
        setattr(
            self, method_name,
            types.MethodType(get, self)
        )


class BaseResource(BaseResource):
    """
    Fix for "type object argument after ** must be a mapping, not NoneType"
    """
    def set_subresources(self, **kwargs):
        """Same logic as the original except for the first 'if' clause."""
        for attribute_name, resource in self._subresource_map.items():
            sub_attr = kwargs.get(attribute_name)
            if sub_attr is None:
                # Attribute was not found or is null
                value = None
            elif isinstance(sub_attr, list):
                # A list of subresources is supported
                value = [resource(**x) for x in sub_attr]
            else:
                # So is a single resource
                value = resource(**sub_attr)
            setattr(self, attribute_name, value)
