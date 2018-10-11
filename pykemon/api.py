#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" pykemon.api

User interaction with this package is done through this file.
"""

from beckett.clients import BaseClient
from . import resourcesV2 as rV2


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
            rV2.GenderResource,
            rV2.GrowthRateResource,
            rV2.NatureResource,
            rV2.PokeathlonStatResource,
            rV2.PokemonResource,
            rV2.PokemonColorResource,
            rV2.PokemonFormResource,
            rV2.PokemonHabitatResource,
            rV2.PokemonShapeResource,
            rV2.PokemonSpeciesResource,
            rV2.StatResource,
            rV2.TypeResource,
            rV2.LanguageResource
        )
