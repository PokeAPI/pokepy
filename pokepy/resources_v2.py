#!/usr/bin/env python
# coding: utf-8

"""
Resources related to the V2 API

Refer to the documentation for more information
(https://pokeapi.co/docs/v2.html)
"""

from beckett.resources import BaseResource as OriginalBaseResource
from beckett.resources import SubResource


class BaseResource(OriginalBaseResource):
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


##############################
# Common Models (SubResources)
##############################


class APIResourceSubResource(SubResource):
    class Meta:
        name = 'API_Resource'
        identifier = 'url'
        attributes = (
            'url',
        )

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.url)


class NamedAPIResourceSubResource(SubResource):
    class Meta:
        name = 'Named_API_Resource'
        identifier = 'name'
        attributes = (
            'name',
            'url'
        )

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class DescriptionSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Description'
        identifier = 'description'
        attributes = (
            'description',
        )
        subresources = {
            'language': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name,
                              self.description.capitalize()[:10] + "...")


class EffectSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Effect'
        identifier = 'effect'
        attributes = (
            'effect',
        )
        subresources = {
            'language': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name,
                              self.effect.capitalize()[:10] + "...")


class EncounterSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Encounter'
        identifier = 'chance'
        attributes = (
            'min_level',
            'max_level',
            'chance'
        )
        subresources = {
            'condition_values': NamedAPIResourceSubResource,
            'method': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s/%s/%s>' % (self.Meta.name, self.min_level,
                                    self.max_level, self.chance)


class FlavorTextSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Flavor_Text'
        identifier = 'flavor_text'
        attributes = (
            'flavor_text',
        )
        subresources = {
            'language': NamedAPIResourceSubResource,
            'version': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name,
                              self.flavor_text.capitalize()[:10] + "...")


class GenerationGameIndexSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Generation_Game_Index'
        identifier = 'game_index'
        attributes = (
            'game_index',
        )
        subresources = {
            'generation': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.game_index)


class MachineVersionDetailSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Machine_Version_Detail'
        identifier = 'machine'
        subresources = {
            'machine': APIResourceSubResource,
            'version_group': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class NameSubResource(BaseResource):
    class Meta:
        name = 'Name'
        identifier = 'name'
        attributes = (
            'name',
        )
        subresources = {
            'language': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class VerboseEffectSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Verbose_Effect'
        identifier = 'effect'
        attributes = (
            'effect',
            'short_effect'
        )
        subresources = {
            'language': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.effect.capitalize())


class VersionEncounterDetailSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Version_Encounter_Detail'
        identifier = 'max_chance'
        attributes = (
            'max_chance',
        )
        subresources = {
            'version': NamedAPIResourceSubResource,
            'encounter_details': EncounterSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.max_chance)


class VersionGameIndexSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Version_Game_Index'
        identifier = 'game_index'
        attributes = (
            'game_index',
        )
        subresources = {
            'version': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.game_index)


class VersionGroupFlavorTextSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Version_Group_Flavor_Text'
        identifier = 'text'
        attributes = (
            'text',
        )
        subresources = {
            'language': NamedAPIResourceSubResource,
            'version_group': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name,
                              self.text.capitalize()[:10] + "...")


##############
# SubResources
##############


class BerryFlavorMapSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Berry_Flavor_Map'
        identifier = 'potency'
        attributes = (
            'potency',
        )
        subresources = {
            'flavor': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.potency)


class FlavorBerryMapSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Flavor_Berry_Map'
        identifier = 'potency'
        attributes = (
            'potency',
        )
        subresources = {
            'berry': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.potency)


class ContestNameSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Contest_Name'
        identifier = 'name'
        attributes = (
            'name',
            'color'
        )
        subresources = {
            'language': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class EvolutionDetailSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Evolution_Detail'
        identifier = 'gender'
        attributes = (
            'gender',
            'min_level',
            'min_happiness',
            'min_beauty',
            'min_affection',
            'needs_overworld_rain',
            'relative_physical_stats',
            'time_of_day',
            'turn_upside_down'
        )
        subresources = {
            'item': NamedAPIResourceSubResource,
            'trigger': NamedAPIResourceSubResource,
            'held_item': NamedAPIResourceSubResource,
            'known_move': NamedAPIResourceSubResource,
            'known_move_type': NamedAPIResourceSubResource,
            'location': NamedAPIResourceSubResource,
            'party_species': NamedAPIResourceSubResource,
            'party_type': NamedAPIResourceSubResource,
            'trade_species': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


# A ChainLink is tricky to implement with beckett because it is recursive.
# The current solution is to have 3 nearly identical ChainLink classes
# (so far, the maximum number of chaining evolutions depth is 3)
# the last one not having the evolves_to subresource, ending the recursion.


class ChainLink2SubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Chain_Link2'
        identifier = 'is_baby'
        attributes = (
            'is_baby',
        )
        subresources = {
            'species': NamedAPIResourceSubResource,
            'evolution_details': EvolutionDetailSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class ChainLink1SubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Chain_Link1'
        identifier = 'is_baby'
        attributes = (
            'is_baby',
        )
        subresources = {
            'species': NamedAPIResourceSubResource,
            'evolution_details': EvolutionDetailSubResource,
            'evolves_to': ChainLink2SubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class ChainLinkSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Chain_Link'
        identifier = 'is_baby'
        attributes = (
            'is_baby',
        )
        subresources = {
            'species': NamedAPIResourceSubResource,
            'evolution_details': EvolutionDetailSubResource,
            'evolves_to': ChainLink1SubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class PokemonEntrySubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon_Entry'
        identifier = 'entry_number'
        attributes = (
            'entry_number',
        )
        subresources = {
            'pokemon_species': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.entry_number)


class ItemSpritesSubResource(SubResource):
    class Meta(BaseResource.Meta):
        name = 'Item_Sprites'
        identifier = 'default'
        attributes = (
            'default',
        )

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name,
                              self.default.capitalize()[:10] + "...")


class ItemHolderPokemonVersionDetailSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Item_Holder_Pokemon_Version_Detail'
        identifier = 'rarity'
        attributes = (
            'rarity',
        )
        subresources = {
            'version': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class ItemHolderPokemonSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Item_Holder_Pokemon'
        identifier = 'pokemon'
        subresources = {
            'pokemon': NamedAPIResourceSubResource,
            'version_details': ItemHolderPokemonVersionDetailSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class ContestComboDetailSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Contest_Combo_Detail'
        identifier = 'use_before'
        subresources = {
            'use_before': NamedAPIResourceSubResource,
            'use_after': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class ContestComboSetsSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Contest_Combo_Sets'
        identifier = 'normal'
        subresources = {
            'normal': ContestComboDetailSubResource,
            'super': ContestComboDetailSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class MoveFlavorTextSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Move_Flavor_Text'
        identifier = 'flavor_text'
        attributes = (
            'flavor_text',
        )
        subresources = {
            'language': NamedAPIResourceSubResource,
            'version_group': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name,
                              self.flavor_text.capitalize()[:10] + "...")


class MoveMetaDataSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Move_Meta_Data'
        identifier = 'min_hits'
        attributes = (
            'min_hits',
            'max_hits',
            'min_turns',
            'max_turns',
            'drain',
            'healing',
            'crit_rate',
            'ailment_chance',
            'flinch_chance',
            'stat_chance'
        )
        subresources = {
            'ailment': NamedAPIResourceSubResource,
            'category': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class MoveStatChangeSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Move_Stat_Change'
        identifier = 'change'
        attributes = (
            'change',
        )
        subresources = {
            'stat': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.change)


class PastMoveStatValuesSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Past_Move_Stat_Values'
        identifier = 'accuracy'
        attributes = (
            'accuracy',
            'effect_chance',
            'power',
            'pp'
        )
        subresources = {
            'effect_entries': VerboseEffectSubResource,
            'type': NamedAPIResourceSubResource,
            'version_group': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class EncounterVersionDetailsSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Encounter_Version_Details'
        identifier = 'rate'
        attributes = (
            'rate',
        )
        subresources = {
            'version': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.rate)


class EncounterMethodRateSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Encounter_Method_Rate'
        identifier = 'encounter_method'
        subresources = {
            'encounter_method': NamedAPIResourceSubResource,
            'version_details': EncounterVersionDetailsSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class PokemonEncounterSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon_Encounter'
        identifier = 'pokemon'
        subresources = {
            'pokemon': NamedAPIResourceSubResource,
            'version_details': VersionEncounterDetailSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class PalParkEncounterSpeciesSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pal_Park_Encounter_Species'
        identifier = 'rate'
        attributes = (
            'base_score',
            'rate'
        )
        subresources = {
            'pokemon_species': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class AbilityEffectChangeSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Ability_Effect_Change'
        identifier = 'effect_entries'
        subresources = {
            'effect_entries': EffectSubResource,
            'version_group': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class AbilityFlavorTextSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Ability_Flavor_Text'
        identifier = 'flavor_text'
        attributes = (
            'flavor_text',
        )
        subresources = {
            'language': NamedAPIResourceSubResource,
            'version_group': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name,
                              self.flavor_text.capitalize()[:10] + "...")


class AbilityPokemonSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Ability_Pokemon'
        identifier = 'slot'
        attributes = (
            'is_hidden',
            'slot'
        )
        subresources = {
            'pokemon': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class PokemonSpeciesGenderSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon_Species_Gender'
        identifier = 'rate'
        attributes = (
            'rate',
        )
        subresources = {
            'pokemon_species': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.rate)


class GrowthRateExperienceLevelSubResource(SubResource):
    class Meta(BaseResource.Meta):
        name = 'Growth_Rate_Experience_Level'
        identifier = 'level'
        attributes = (
            'level',
            'experience'
        )

    def __repr__(self):
        return '<%s - %s/%s>' % (self.Meta.name, self.level, self.experience)


class NatureStatChangeSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Nature_Stat_Change'
        identifier = 'max_change'
        attributes = (
            'max_change',
        )
        subresources = {
            'pokeathlon_stat': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.max_change)


class MoveBattleStylePreferenceSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Move_Battle_Style_Preference'
        identifier = 'low_hp_preference'
        attributes = (
            'low_hp_preference',
            'high_hp_preference'
        )
        subresources = {
            'move_battle_style': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s/%s>' % (self.Meta.name, self.low_hp_preference,
                                 self.high_hp_preference)


class NaturePokeathlonStatAffectSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Nature_Pokeathlon_Stat_Affect'
        identifier = 'max_change'
        attributes = (
            'max_change',
        )
        subresources = {
            'nature': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.max_change)


class NaturePokeathlonStatAffectSetsSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Nature_Pokeathlon_Stat_Affect_Sets'
        identifier = 'increase'
        subresources = {
            'increase': NaturePokeathlonStatAffectSubResource,
            'decrease': NaturePokeathlonStatAffectSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class PokemonAbilitySubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon_Ability'
        identifier = 'is_hidden'
        attributes = (
            'is_hidden',
            'slot'
        )
        subresources = {
            'ability': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class PokemonTypeSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon_Type'
        identifier = 'slot'
        attributes = (
            'slot',
        )
        subresources = {
            'type': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class PokemonHeldItemVersionSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon_Held_Item_Version'
        identifier = 'rarity'
        attributes = (
            'rarity',
        )
        subresources = {
            'version': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class PokemonHeldItemSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon_Held_Item'
        identifier = 'item'
        subresources = {
            'item': NamedAPIResourceSubResource,
            'version_details': PokemonHeldItemVersionSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class PokemonMoveVersionSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon_Move_Version'
        identifier = 'level_learned_at'
        attributes = (
            'level_learned_at',
        )
        subresources = {
            'move_learn_method': NamedAPIResourceSubResource,
            'version_group': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class PokemonMoveSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon_Move'
        identifier = 'move'
        subresources = {
            'move': NamedAPIResourceSubResource,
            'version_group_details': PokemonMoveVersionSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class PokemonStatSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon_Stat'
        identifier = 'effort'
        attributes = (
            'effort',
            'base_stat'
        )
        subresources = {
            'stat': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class PokemonSpritesSubResource(SubResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon_Sprites'
        identifier = 'front_default'
        attributes = (
            'front_default',
            'front_shiny',
            'front_female',
            'front_shiny_female',
            'back_default',
            'back_shiny',
            'back_female',
            'back_shiny_female',
        )

    def __repr__(self):
        return '<%s>' % self.Meta.name


class LocationAreaEncounterSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Location_Area_Encounter'
        identifier = 'location_area'
        subresources = {
            'location_area': NamedAPIResourceSubResource,
            'version_details': VersionEncounterDetailSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class PokemonFormSpritesSubResource(SubResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon_Form_Sprites'
        identifier = 'front_default'
        attributes = (
            'front_default',
            'front_shiny',
            'back_default',
            'back_shiny'
        )

    def __repr__(self):
        return '<%s>' % self.Meta.name


class AwesomeNameSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Awesome_Name'
        identifier = 'awesome_name'
        attributes = (
            'awesome_name',
        )
        subresources = {
            'language': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.awesome_name.capitalize())


class GenusSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Genus'
        identifier = 'genus'
        attributes = (
            'genus',
        )
        subresources = {
            'language': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.genus.capitalize())


class PokemonSpeciesDexEntrySubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon_Species_Dex_Entry'
        identifier = 'entry_number'
        attributes = (
            'entry_number',
        )
        subresources = {
            'pokedex': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.entry_number)


class PalParkEncounterAreaSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pal_Park_Encounter_Area'
        identifier = 'base_score'
        attributes = (
            'base_score',
            'rate'
        )
        subresources = {
            'area': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class PokemonSpeciesVarietySubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon_Species_Variety'
        identifier = 'is_default'
        attributes = (
            'is_default',
        )
        subresources = {
            'pokemon': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class MoveStatAffectSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Move_Stat_Affect'
        identifier = 'change'
        attributes = (
            'change',
        )
        subresources = {
            'move': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class MoveStatAffectSetsSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Move_Stat_Affect_Sets'
        identifier = 'increase'
        subresources = {
            'increase': MoveStatAffectSubResource,
            'decrease': MoveStatAffectSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class NatureStatAffectSetsSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Nature_Stat_Affect_Sets'
        identifier = 'increase'
        subresources = {
            'increase': NamedAPIResourceSubResource,
            'decrease': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class TypePokemonSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Type_Pokemon'
        identifier = 'slot'
        attributes = (
            'slot',
        )
        subresources = {
            'pokemon': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


class TypeRelationsSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Type_Relations'
        identifier = 'no_damage_to'
        subresources = {
            'no_damage_to': NamedAPIResourceSubResource,
            'half_damage_to': NamedAPIResourceSubResource,
            'double_damage_to': NamedAPIResourceSubResource,
            'no_damage_from': NamedAPIResourceSubResource,
            'half_damage_from': NamedAPIResourceSubResource,
            'double_damage_from': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s>' % self.Meta.name


###########
# Resources
###########


class BerryResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Berry'
        resource_name = 'berry'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
            'growth_time',
            'max_harvest',
            'natural_gift_power',
            'size',
            'smoothness',
            'soil_dryness'
        )
        subresources = {
            'firmness': NamedAPIResourceSubResource,
            'flavors': BerryFlavorMapSubResource,
            'item': NamedAPIResourceSubResource,
            'natural_gift_type': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class BerryFirmnessResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Berry_Firmness'
        resource_name = 'berry-firmness'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'berries': NamedAPIResourceSubResource,
            'names': NameSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class BerryFlavorResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Berry_Flavor'
        resource_name = 'berry-flavor'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'berries': FlavorBerryMapSubResource,
            'contest_type': NamedAPIResourceSubResource,
            'names': NameSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class ContestTypeResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Contest_Type'
        resource_name = 'contest-type'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'berry_flavor': NamedAPIResourceSubResource,
            'names': ContestNameSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class ContestEffectResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Contest_Effect'
        resource_name = 'contest-effect'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'appeal',
            'jam'
        )
        subresources = {
            'effect_entries': EffectSubResource,
            'flavor_text_entries': FlavorTextSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.id)


class SuperContestEffectResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Super_Contest_Effect'
        resource_name = 'super-contest-effect'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'appeal'
        )
        subresources = {
            'flavor_text_entries': FlavorTextSubResource,
            'moves': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.id)


class EncounterMethodResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Encounter_Method'
        resource_name = 'encounter-method'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
            'order'
        )
        subresources = {
            'names': NameSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class EncounterConditionResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Encounter_Condition'
        resource_name = 'encounter-condition'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'names': NameSubResource,
            'values': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class EncounterConditionValueResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Encounter_Condition_Value'
        resource_name = 'encounter-condition-value'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'condition': NamedAPIResourceSubResource,
            'names': NameSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class EvolutionChainResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Evolution_Chain'
        resource_name = 'evolution-chain'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
        )
        subresources = {
            'baby_trigger_item': NamedAPIResourceSubResource,
            'chain': ChainLinkSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.id)


class EvolutionTriggerResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Evolution_Trigger'
        resource_name = 'evolution-trigger'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'names': NameSubResource,
            'pokemon_species': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class GenerationResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Generation'
        resource_name = 'generation'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'abilities': NamedAPIResourceSubResource,
            'names': NameSubResource,
            'main_region': NamedAPIResourceSubResource,
            'moves': NamedAPIResourceSubResource,
            'pokemon_species': NamedAPIResourceSubResource,
            'types': NamedAPIResourceSubResource,
            'version_groups': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class PokedexResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Pokedex'
        resource_name = 'pokedex'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
            'is_main_series'
        )
        subresources = {
            'descriptions': DescriptionSubResource,
            'names': NameSubResource,
            'pokemon_entries': PokemonEntrySubResource,
            'region': NamedAPIResourceSubResource,
            'version_groups': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class VersionResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Version'
        resource_name = 'version'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'names': NameSubResource,
            'version_group': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class VersionGroupResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Version_Group'
        resource_name = 'version-group'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
            'order'
        )
        subresources = {
            'generation': NamedAPIResourceSubResource,
            'move_learn_methods': NamedAPIResourceSubResource,
            'pokedexes': NamedAPIResourceSubResource,
            'regions': NamedAPIResourceSubResource,
            'versions': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class ItemCategoryResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Item_Category'
        resource_name = 'item-category'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'items': NamedAPIResourceSubResource,
            'names': NameSubResource,
            'pocket': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class ItemResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Item'
        resource_name = 'item'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
            'cost',
            'fling_power'
        )
        subresources = {
            'fling_effect': NamedAPIResourceSubResource,
            'attributes': NamedAPIResourceSubResource,
            'category': NamedAPIResourceSubResource,
            'effect_entries': VerboseEffectSubResource,
            'flavor_text_entries': VersionGroupFlavorTextSubResource,
            'game_indices': GenerationGameIndexSubResource,
            'names': NameSubResource,
            'sprites': ItemSpritesSubResource,
            'held_by_pokemon': ItemHolderPokemonSubResource,
            'baby_trigger_for': APIResourceSubResource,
            'machines': MachineVersionDetailSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class ItemAttributeResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Item_Attribute'
        resource_name = 'item-attribute'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'items': NamedAPIResourceSubResource,
            'names': NameSubResource,
            'descriptions': DescriptionSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class ItemFlingEffectResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Item_Fling_Effect'
        resource_name = 'item-fling-effect'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'effect_entries': EffectSubResource,
            'items': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class ItemPocketResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Item_Pocket'
        resource_name = 'item-pocket'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'categories': NamedAPIResourceSubResource,
            'names': NameSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class MachineResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Machine'
        resource_name = 'machine'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
        )
        subresources = {
            'item': NamedAPIResourceSubResource,
            'move': NamedAPIResourceSubResource,
            'version_group': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.id)


class MoveResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Move'
        resource_name = 'move'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
            'accuracy',
            'effect_chance',
            'pp',
            'priority',
            'power'
        )
        subresources = {
            'contest_combos': ContestComboSetsSubResource,
            'contest_type': NamedAPIResourceSubResource,
            'contest_effect': APIResourceSubResource,
            'damage_class': NamedAPIResourceSubResource,
            'effect_entries': VerboseEffectSubResource,
            'effect_changes': AbilityEffectChangeSubResource,
            'flavor_text_entries': MoveFlavorTextSubResource,
            'generation': NamedAPIResourceSubResource,
            'machines': MachineVersionDetailSubResource,
            'meta': MoveMetaDataSubResource,
            'names': NameSubResource,
            'past_values': PastMoveStatValuesSubResource,
            'stat_changes': MoveStatChangeSubResource,
            'super_contest_effect': APIResourceSubResource,
            'target': NamedAPIResourceSubResource,
            'type': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class MoveAilmentResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Move_Ailment'
        resource_name = 'move-ailment'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'moves': NamedAPIResourceSubResource,
            'names': NameSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class MoveBattleStyleResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Move_Battle_Style'
        resource_name = 'move-battle-style'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'names': NameSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class MoveCategoryResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Move_Category'
        resource_name = 'move-category'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'moves': NamedAPIResourceSubResource,
            'descriptions': DescriptionSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class MoveDamageClassResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Move_Damage_Class'
        resource_name = 'move-damage-class'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'descriptions': DescriptionSubResource,
            'moves': NamedAPIResourceSubResource,
            'names': NameSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class MoveLearnMethodResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Move_Learn_Method'
        resource_name = 'move-learn-method'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'descriptions': DescriptionSubResource,
            'names': NameSubResource,
            'version_groups': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class MoveTargetResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Move_Target'
        resource_name = 'move-target'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'descriptions': DescriptionSubResource,
            'moves': NamedAPIResourceSubResource,
            'names': NameSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class LocationResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Location'
        resource_name = 'location'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'region': NamedAPIResourceSubResource,
            'names': NameSubResource,
            'game_indices': GenerationGameIndexSubResource,
            'areas': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class LocationAreaResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Location_Area'
        resource_name = 'location-area'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
            'game_index'
        )
        subresources = {
            'encounter_method_rates': EncounterMethodRateSubResource,
            'location': NamedAPIResourceSubResource,
            'names': NameSubResource,
            'pokemon_encounters': PokemonEncounterSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class PalParkAreaResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Pal_Park_Area'
        resource_name = 'pal-park-area'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'names': NameSubResource,
            'pokemon_encounters': PalParkEncounterSpeciesSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class RegionResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Region'
        resource_name = 'region'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'locations': NamedAPIResourceSubResource,
            'main_generation': NamedAPIResourceSubResource,
            'names': NameSubResource,
            'pokedexes': NamedAPIResourceSubResource,
            'version_groups': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class AbilityResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Ability'
        resource_name = 'ability'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
            'is_main_series'
        )
        subresources = {
            'generation': NamedAPIResourceSubResource,
            'names': NameSubResource,
            'effect_entries': VerboseEffectSubResource,
            'effect_changes': AbilityEffectChangeSubResource,
            'flavor_text_entries': AbilityFlavorTextSubResource,
            'pokemon': AbilityPokemonSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class CharacteristicResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Characteristic'
        resource_name = 'characteristic'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'gene_modulo',
            'possible_values'
        )
        subresources = {
            'descriptions': DescriptionSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.id)


class EggGroupResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Egg_Group'
        resource_name = 'egg-group'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'names': NameSubResource,
            'pokemon_species': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class GenderResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Gender'
        resource_name = 'gender'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name'
        )
        subresources = {
            'pokemon_species_details': PokemonSpeciesGenderSubResource,
            'required_for_evolution': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class GrowthRateResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Growth_Rate'
        resource_name = 'growth-rate'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
            'formula'
        )
        subresources = {
            'descriptions': DescriptionSubResource,
            'levels': GrowthRateExperienceLevelSubResource,
            'pokemon_species': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class NatureResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Nature'
        resource_name = 'nature'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
        )
        subresources = {
            'decreased_stat': NamedAPIResourceSubResource,
            'increased_stat': NamedAPIResourceSubResource,
            'hates_flavor': NamedAPIResourceSubResource,
            'likes_flavor': NamedAPIResourceSubResource,
            'pokeathlon_stat_changes': NatureStatChangeSubResource,
            'move_battle_style_preferences': MoveBattleStylePreferenceSubResource,
            'names': NameSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class PokeathlonStatResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Pokeathlon_Stat'
        resource_name = 'pokeathlon-stat'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
        )
        subresources = {
            'names': NameSubResource,
            'affecting_natures': NaturePokeathlonStatAffectSetsSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class PokemonResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Pokemon'
        resource_name = 'pokemon'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
            'base_experience',
            'height',
            'is_default',
            'order',
            'weight',
            'location_area_encounters'
        )
        subresources = {
            'abilities': PokemonAbilitySubResource,
            'forms': NamedAPIResourceSubResource,
            'game_indices': VersionGameIndexSubResource,
            'held_items': PokemonHeldItemSubResource,
            'moves': PokemonMoveSubResource,
            'sprites': PokemonSpritesSubResource,
            'species': NamedAPIResourceSubResource,
            'stats': PokemonStatSubResource,
            'types': PokemonTypeSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class PokemonColorResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Pokemon_Color'
        resource_name = 'pokemon-color'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
        )
        subresources = {
            'names': NameSubResource,
            'pokemon_species': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class PokemonFormResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Pokemon_Form'
        resource_name = 'pokemon-form'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
            'order',
            'form_order',
            'is_default',
            'is_battle_only',
            'is_mega',
            'form_name',
        )
        subresources = {
            'pokemon': NamedAPIResourceSubResource,
            'sprites': PokemonFormSpritesSubResource,
            'version_group': NamedAPIResourceSubResource,
            'names': NameSubResource,
            'form_names': NameSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class PokemonHabitatResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Pokemon_Habitat'
        resource_name = 'pokemon-habitat'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
        )
        subresources = {
            'names': NameSubResource,
            'pokemon_species': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class PokemonShapeResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Pokemon_Shape'
        resource_name = 'pokemon-shape'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
        )
        subresources = {
            'awesome_names': AwesomeNameSubResource,
            'names': NameSubResource,
            'pokemon_species': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class PokemonSpeciesResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Pokemon_Species'
        resource_name = 'pokemon-species'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
            'order',
            'gender_rate',
            'capture_rate',
            'base_happiness',
            'is_baby',
            'is_legendary',
            'is_mythical',
            'hatch_counter',
            'has_gender_differences',
            'forms_switchable',
        )
        subresources = {
            'growth_rate': NamedAPIResourceSubResource,
            'pokedex_numbers': PokemonSpeciesDexEntrySubResource,
            'egg_groups': NamedAPIResourceSubResource,
            'color': NamedAPIResourceSubResource,
            'shape': NamedAPIResourceSubResource,
            'evolves_from_species': NamedAPIResourceSubResource,
            'evolution_chain': APIResourceSubResource,
            'habitat': NamedAPIResourceSubResource,
            'generation': NamedAPIResourceSubResource,
            'names': NameSubResource,
            'pal_park_encounters': PalParkEncounterAreaSubResource,
            'flavor_text_entries': FlavorTextSubResource,
            'form_descriptions': DescriptionSubResource,
            'genera': GenusSubResource,
            'varieties': PokemonSpeciesVarietySubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class StatResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Stat'
        resource_name = 'stat'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
            'game_index',
            'is_battle_only',
        )
        subresources = {
            'affecting_moves': MoveStatAffectSetsSubResource,
            'affecting_natures': NatureStatAffectSetsSubResource,
            'characteristics': APIResourceSubResource,
            'move_damage_class': NamedAPIResourceSubResource,
            'names': NameSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class TypeResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Type'
        resource_name = 'type'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
        )
        subresources = {
            'damage_relations': TypeRelationsSubResource,
            'game_indices': GenerationGameIndexSubResource,
            'generation': NamedAPIResourceSubResource,
            'move_damage_class': NamedAPIResourceSubResource,
            'names': NameSubResource,
            'pokemon': TypePokemonSubResource,
            'moves': NamedAPIResourceSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class LanguageResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Language'
        resource_name = 'language'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
            'official',
            'iso639',
            'iso3166',
        )
        subresources = {
            'names': NameSubResource
        }

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())
