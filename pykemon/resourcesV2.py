# -*- coding: utf-8 -*-

from beckett.resources import BaseResource, SubResource


# Common Models (SubResources)


class APIResourceSubResource(SubResource):
    class Meta:
        name = 'API_Resource'
        identifier = 'url'
        attributes = (
            'url'
        )


class NamedAPIResourceSubResource(SubResource):
    class Meta:
        name = 'Named_API_Resource'
        identifier = 'name'
        attributes = (
            'name',
            'url'
        )


class DescriptionSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Description'
        resource_name = 'description'
        identifier = 'description'
        attributes = (
            'description',
        )
        subresources = {
            'language': NamedAPIResourceSubResource
        }


class EffectSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Effect'
        resource_name = 'effect'
        identifier = 'effect'
        attributes = (
            'effect',
        )
        subresources = {
            'language': NamedAPIResourceSubResource
        }


class EncounterSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Encounter'
        resource_name = 'encounter'
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


class FlavorTextSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Flavor_Text'
        resource_name = 'flavor-text'
        identifier = 'flavor_text'
        attributes = (
            'flavor_text',
        )
        subresources = {
            'language': NamedAPIResourceSubResource
        }


class GenerationGameIndexSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Generation_Game_Index'
        resource_name = 'generation-game-index'
        identifier = 'game_index'
        attributes = (
            'game_index',
        )
        subresources = {
            'generation': NamedAPIResourceSubResource
        }


class MachineVersionDetailSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Machine_Version_Detail'
        resource_name = 'machine-version-detail'
        identifier = 'machine'
        subresources = {
            'machine': APIResourceSubResource,
            'version_group': NamedAPIResourceSubResource
        }


class NameSubResource(BaseResource):
    class Meta:
        name = 'Name'
        resource_name = 'name'
        identifier = 'name'
        attributes = (
            'name',
        )
        subresources = {
            'language': NamedAPIResourceSubResource
        }


class VerboseEffectSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Verbose_Effect'
        resource_name = 'verbose-effect'
        identifier = 'effect'
        attributes = (
            'effect',
            'short_effect'
        )
        subresources = {
            'language': NamedAPIResourceSubResource
        }


class VersionEncounterDetailSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Version_Encounter_Detail'
        resource_name = 'verbose-encounter-detail'
        identifier = 'max_chance'
        attributes = (
            'max_chance'
        )
        subresources = {
            'version': NamedAPIResourceSubResource,
            'encounter_details': EncounterSubResource
        }


class VersionGameIndexSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Version_Game_Index'
        resource_name = 'version-Game-index'
        identifier = 'game_index'
        attributes = (
            'game_index'
        )
        subresources = {
            'version': NamedAPIResourceSubResource
        }


class VersionGroupFlavorTextSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Version_Group_Flavor_Text'
        resource_name = 'version-Group-flavor-text'
        identifier = 'text'
        attributes = (
            'text'
        )
        subresources = {
            'language': NamedAPIResourceSubResource,
            'version_group': NamedAPIResourceSubResource
        }


# SubResources


class BerryFlavorMapSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Berry_Flavor_Map'
        resource_name = 'berry-flavor-map'
        identifier = 'potency'
        attributes = (
            'potency',
        )
        subresources = {
            'flavor': NamedAPIResourceSubResource
        }


class FlavorBerryMapSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Flavor_Berry_Map'
        resource_name = 'flavor-berry-map'
        identifier = 'potency'
        attributes = (
            'potency',
        )
        subresources = {
            'berry': NamedAPIResourceSubResource
        }


class ContestNameSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Contest_Name'
        resource_name = 'contest-name'
        identifier = 'name'
        attributes = (
            'name',
            'color'
        )
        subresources = {
            'language': NamedAPIResourceSubResource
        }


class EvolutionDetailSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Evolution_Detail'
        resource_name = 'evolution-detail'
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


class ChainLinkSubResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Chain_Link'
        resource_name = 'chain-link'
        identifier = 'is_baby'
        attributes = (
            'is_baby'
        )
        subresources = {
            'species': NamedAPIResourceSubResource,
            'evolution_details': EvolutionDetailSubResource,
            # 'evolves_to': lambda **kwargs: ChainLinkSubResource  # TODO - Not working correctly...
        }



















































# Resources


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
            'name',
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
            'name',
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
        name = 'Contest_type'
        resource_name = 'contest-type'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'id',
            'name',
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
            'jam',
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
            'appeal',
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
            'order',
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
            'name',
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
            'name',
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
            # 'baby_trigger_item': NamedAPIResourceSubResource,  # TODO - Throws error when null is returned
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
            'name',
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
            'name',
            'abilities',
            'names',
            'main_region',
            'moves',
            'pokemon_species',
            'types',
            'version_groups'
        )

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
            'is_main_series',
            'descriptions',
            'names',
            'pokemon_entries',
            'region',
            'version_groups'
        )

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
            'name',
            'names',
            'version_group'
        )

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
            'order',
            'generation',
            'move_learn_methods',
            'pokedexes',
            'regions',
            'versions'
        )

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
            'fling_power',
            'fling_effect',
            'attributes',
            'category',
            'effect_entries',
            'flavor_text_entries',
            'game_indices',
            'names',
            'sprites',
            'held_by_pokemon',
            'baby_trigger_for',
            'machines'
        )

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
            'name',
            'items',
            'names',
            'descriptions'
        )

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
            'name',
            'items',
            'names',
            'pocket'
        )

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
            'name',
            'effect_entries',
            'items'
        )

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
            'name',
            'categories',
            'names'
        )

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
            'item',
            'move',
            'version_group'
        )

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
            'power',
            'contest_combos',
            'contest_type',
            'contest_effect',
            'damage_class',
            'effect_entries',
            'effect_changes',
            'flavor_text_entries',
            'generation',
            'machines',
            'meta',
            'names',
            'past_values',
            'stat_changes',
            'super_contest_effect',
            'target',
            'type'
        )

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
            'name',
            'moves',
            'names'
        )

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
            'name',
            'names'
        )

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
            'name',
            'moves',
            'descriptions'
        )

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
            'name',
            'descriptions',
            'moves',
            'names'
        )

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
            'name',
            'descriptions',
            'names',
            'version_groups'
        )

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
            'name',
            'descriptions',
            'moves',
            'names'
        )

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
            'name',
            'region',
            'names',
            'game_indices',
            'areas'
        )

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
            'game_index',
            'encounter_method_rates',
            'location',
            'names',
            'pokemon_encounters'
        )

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
            'name',
            'names',
            'pokemon_encounters'
        )

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
            'name',
            'locations',
            'main_generation',
            'names',
            'pokedexes',
            'version_groups'
        )

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
            'is_main_series',
            'generation',
            'names',
            'effect_entries',
            'effect_changes',
            'flavor_text_entries',
            'pokemon'
        )

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
            'possible_values',
            'descriptions'
        )

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
            'name',
            'names',
            'pokemon_species'
        )

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
            'name',
            'pokemon_species_details',
            'required_for_evolution'
        )

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
            'formula',
            'descriptions',
            'levels',
            'pokemon_species'
        )

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
            'decreased_stat',
            'increased_stat',
            'hates_flavor',
            'likes_flavor',
            'pokeathlon_stat_changes',
            'move_battle_style_preferences',
            'names'
        )

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
            'names',
            'affecting_natures'
        )

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
            'abilities',
            'forms',
            'game_indices',
            'held_items',
            'location_area_encounters',
            'moves',
            'sprites',
            'species',
            'stats',
            'types'
        )

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
            'names',
            'pokemon_species',
        )

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
            'pokemon',
            'sprites',
            'version_group',
            'names',
            'form_names'
        )

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
            'names',
            'pokemon_species'
        )

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
            'awesome_names',
            'names',
            'pokemon_species'
        )

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
            'hatch_counter',
            'has_gender_differences',
            'forms_switchable',
            'growth_rate',
            'pokedex_numbers',
            'egg_groups',
            'color',
            'shape',
            'evolves_from_species',
            'evolution_chain',
            'habitat',
            'generation',
            'names',
            'pal_park_encounters',
            'flavor_text_entries',
            'form_descriptions',
            'genera',
            'varieties'
        )

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
            'affecting_moves',
            'affecting_natures',
            'characteristics',
            'move_damage_class',
            'names'
        )

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
            'damage_relations',
            'game_indices',
            'generation',
            'move_damage_class',
            'names',
            'pokemon',
            'moves'
        )

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
            'names'
        )

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())
