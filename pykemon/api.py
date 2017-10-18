#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" pykemon.api

User interaction with this package is done through this file.
"""

from beckett.clients import BaseClient

import resourcesV1 as rV1
import resourcesV2 as rV2


class V1Client(BaseClient):

    class Meta(BaseClient.Meta):
        name = 'pykemon-v1-client'
        base_url = 'https://pokeapi.co/api/v1'
        resources = (
            rV1.PokedexResource,
            rV1.MoveResource,
            rV1.PokemonResource,
            rV1.TypeResource,
            rV1.AbilityResource,
            rV1.EggResource,
            rV1.DescriptionResource,
            rV1.SpriteResource,
            rV1.GameResource
        )


class V2Client(BaseClient):

    class Meta(BaseClient.Meta):
        name = 'pykemon-v2-client'
        base_url = 'https://pokeapi.co/api/v2'
        resources = (
            rV2.BerryResource,
            rV2.BerryFirmnessResource,
            rV2.BerryFlavorResource,
            rV2.ContestTypeResource,
            rV2.ContestEffectResource,
            rV2.SuperContestEffectResource,
            rV2.EncounterMethodResource,
            rV2.EncounterConditionResource,
            rV2.EncounterConditionValueResource,
            rV2.EvolutionChainResource,
            rV2.EvolutionTriggerResource,
            rV2.GenerationResource,
            rV2.PokedexResource,
            rV2.VersionResource,
            rV2.VersionGroupResource,
            rV2.ItemResource,
            rV2.ItemAttributeResource,
            rV2.ItemCategoryResource,
            rV2.ItemFlingEffectResource,
            rV2.ItemPocketResource,
            rV2.MachineResource,
            rV2.MoveResource,
            rV2.MoveAilmentResource,
            rV2.MoveBattleStyleResource,
            rV2.MoveCategoryResource,
            rV2.MoveDamageClassResource,
            rV2.MoveLearnMethodResource,
            rV2.MoveTargetResource,
            rV2.LocationResource,
            rV2.LocationAreaResource,
            rV2.PalParkAreaResource,
            rV2.RegionResource,
            rV2.AbilityResource,
            rV2.CharacteristicResource,
            rV2.EggGroupResource,
            rV2.GenderResource
        )
