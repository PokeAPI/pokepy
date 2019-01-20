#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" pokepy.api

User interaction with this package is done through this file.
"""

from .beckett_tweaks import BaseClient
from . import resources_v2 as rv2


class V2Client(BaseClient):
    """Pokeapi client"""

    class Meta(BaseClient.Meta):
        name = 'pokepy-v2-client'
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
