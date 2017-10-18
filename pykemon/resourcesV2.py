# -*- coding: utf-8 -*-

from beckett.resources import BaseResource


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
            'soil_dryness',
            'firmness',
            'flavors',
            'item',
            'natural_gift_type'
        )

    def __repr__(self):
        return '<Berry - %s>' % self.name.capitalize()


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
            'berries',
            'names'
        )

    def __repr__(self):
        return '<Berry_Firmness - %s>' % self.name.capitalize()


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
            'berries',
            'contest_type',
            'names'
        )

    def __repr__(self):
        return '<Berry_Flavor - %s>' % self.name.capitalize()


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
            'berry_flavor',
            'names'
        )

    def __repr__(self):
        return '<Contest_Type - %s>' % self.name.capitalize()


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
            'effect_entries',
            'flavor_text_entries'
        )

    def __repr__(self):
        return '<Contest_Effect - %s>' % self.id


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
            'flavor_text_entries',
            'moves'
        )

    def __repr__(self):
        return '<Super_Contest_Effect - %s>' % self.id


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
            'names'
        )

    def __repr__(self):
        return '<Encounter_Method - %s>' % self.name.capitalize()


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
            'names',
            'values'
        )

    def __repr__(self):
        return '<Encounter_Condition - %s>' % self.name.capitalize()


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
            'condition',
            'names'
        )

    def __repr__(self):
        return '<Encounter_Condition_Value - %s>' % self.name.capitalize()


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
            'baby_trigger_item',
            'chain'
        )

    def __repr__(self):
        return '<Evolution_Chain - %s>' % self.id


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
            'names',
            'pokemon_species'
        )

    def __repr__(self):
        return '<Evolution_Trigger - %s>' % self.name.capitalize()


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
        return '<Generation - %s>' % self.name.capitalize()


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
        return '<Pokedex - %s>' % self.name.capitalize()


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
        return '<Version - %s>' % self.name.capitalize()


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
        return '<Version_Group - %s>' % self.name.capitalize()


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
        return '<Item - %s>' % self.name.capitalize()


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
        return '<Item_Attribute - %s>' % self.name.capitalize()


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
        return '<Item_Category - %s>' % self.name.capitalize()


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
        return '<Item_Fling_Effect - %s>' % self.name.capitalize()


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
        return '<Item_Pocket - %s>' % self.name.capitalize()


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
        return '<Machine - %s>' % self.id


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
        return '<Move - %s>' % self.name.capitalize()


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
        return '<Move_Ailment - %s>' % self.name.capitalize()


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
        return '<Move_Battle_Style - %s>' % self.name.capitalize()


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
        return '<Move_Category - %s>' % self.name.capitalize()


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
        return '<Move_Damage_Class - %s>' % self.name.capitalize()


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
        return '<Move_Learn_Method - %s>' % self.name.capitalize()


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
        return '<Move_Target - %s>' % self.name.capitalize()


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
        return '<Location - %s>' % self.name.capitalize()


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
        return '<Location_Area - %s>' % self.name.capitalize()


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
        return '<Pal_Park_Area - %s>' % self.name.capitalize()


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
        return '<Region - %s>' % self.name.capitalize()


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
        return '<Ability - %s>' % self.name.capitalize()


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
        return '<Characteristic - %s>' % self.id


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
        return '<Egg_Group - %s>' % self.name.capitalize()


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
        return '<Gender - %s>' % self.name.capitalize()


























class XXXXXXXXXResource(BaseResource):

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
        return '<Gender - %s>' % self.name.capitalize()