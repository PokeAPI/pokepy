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
