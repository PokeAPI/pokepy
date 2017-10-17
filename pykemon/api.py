#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" pykemon.api

User interaction with this package is done through this file.
"""

from beckett.clients import BaseClient

from resourcesV1 import (
    MoveResource, PokemonResource, TypeResource, AbilityResource,
    EggResource, DescriptionResource, SpriteResource, GameResource
)


class V1Client(BaseClient):

    class Meta(BaseClient.Meta):
        name = 'pykemon-v1-client'
        base_url = 'https://pokeapi.co/api/v1'
        resources = (
            MoveResource,
            PokemonResource,
            TypeResource,
            AbilityResource,
            EggResource,
            DescriptionResource,
            SpriteResource,
            GameResource,
        )


class V2Client(BaseClient):

    class Meta(BaseClient.Meta):
        name = 'pykemon-v2-client'
        base_url = 'https://pokeapi.co/api/v2'
        resources = (
            # TODO
        )
