#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tweaks to the beckett API plus other new functionality
"""

import functools
import types
import diskcache
from beckett.constants import DEFAULT_VALID_STATUS_CODES
from beckett.clients import BaseClient
from beckett.resources import BaseResource


class BaseClient(BaseClient):
    """
    Tweaks:
        - Allow resources to be called without having to specify 'uid='.
            ex:

                >> client.get_pokemon('bulbasaur')
                >> [<Pokemon - Bulbasaur>]
        - Removed all http methods except GET
        - Added in memory and in disk cache
    """
    def __init__(self, cache=None, cache_location=None, in_disk_expire=None, *args, **kwargs):
        """
        :param cache: str
            cache can be 'in_memory' or 'in_disk',
            for memory-based or disk-based cache, respectively
        :param cache_location: str
            cache directory (for disk-based cache)
            (mandatory when cache='in_disk')
        :param in_disk_expire: float
            seconds until arguments cached expire
            (optional)
        """
        # TODO FanoutCache.memoize is only saving the last function call and not each call with different parameters
        # TODO FanoutCache.memoize cache isn't reloaded with each restart
        if cache == 'in_memory':
            cache_function = functools.partial(functools.lru_cache, maxsize=None)
        elif cache == 'in_disk':
            cache_function = functools.partial(diskcache.FanoutCache(cache_location, shards=1, timeout=1).memoize,
                                               expire=in_disk_expire)
            # # TODO must have cache_info() and cache_clear() as in in_memory
            # def in_disk():
            #     fanout_cache = diskcache.FanoutCache(cache_location, shards=1, timeout=1)
            #
            #     def inner(func):
            #         def cache_info():
            #             return fanout_cache.stats()
            #
            #         def cache_clear():
            #             return fanout_cache.clear()
            #
            #         memoize = fanout_cache.memoize(expire=in_disk_expire)
            #
            #         memoize.cache_info = cache_info
            #         memoize.cache_clear = cache_clear
            #
            #         return memoize(func)
            #
            #     return inner
            #
            # cache_function = in_disk
        else:
            # empty wrapping function
            def no_cache():
                def inner(func):
                    return func
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
        @self.cache()
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
