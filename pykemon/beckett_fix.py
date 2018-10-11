#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fix for
"type object argument after ** must be a mapping, not NoneType" error
"""

from beckett.resources import BaseResource


class BaseResource(BaseResource):

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
