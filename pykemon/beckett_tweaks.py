#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fix for
"type object argument after ** must be a mapping, not NoneType" error
"""

import types
from beckett.constants import DEFAULT_VALID_STATUS_CODES
from beckett.clients import BaseClient
from beckett.resources import BaseResource


class BaseClient(BaseClient):
    """
    Tweak that allows resources to be called
    without having to specify 'uid='.
    ex:

        >> client.get_pokemon('bulbasaur')
        >> [<Pokemon - Bulbasaur>]
    """
    def _assign_method(self, resource_class, method_type):
        """Exactly the same code as the original

        Ignored the other http methods,
        as they are not needed for the pokeapi.co API"""
        method_name = resource_class.get_method_name(
            resource_class, method_type)
        valid_status_codes = getattr(
            resource_class.Meta,
            'valid_status_codes',
            DEFAULT_VALID_STATUS_CODES
        )

        # uid is now right after self
        def get(self, uid=None, method_type=method_type,
                method_name=method_name,
                valid_status_codes=valid_status_codes,
                resource=resource_class, data=None, **kwargs):
            return self.call_api(
                method_type, method_name,
                valid_status_codes, resource,
                data, uid=uid, **kwargs)

        method_map = {
            'GET': get
        }

        setattr(
            self, method_name,
            types.MethodType(method_map[method_type], self)
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
