# -*- coding: utf-8 -*-

""" Resources related to the V1 API

Refer to the documentation for more information (https://pokeapi.co/docsv1/)
"""

from beckett.resources import BaseResource


class PokedexResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Pokedex'
        resource_name = 'pokedex'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'name',
            'created',
            'pokemon',
            'modified'
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
            'name',
            'national_id',
            'created',
            'modified',
            'abilities',
            'egg_groups',
            'evolutions',
            'descriptions',
            'moves',
            'types',
            'catch_rate',
            'species',
            'hp',
            'attack',
            'defense',
            'sp_atk',
            'sp_def',
            'total',
            'speed',
            'egg_cycles',
            'ev_yield',
            'exp',
            'growth_rate',
            'height',
            'weight',
            'male_female_ratio',
            'happiness',
            'sprites'
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
            'name',
            'id',
            'created',
            'modified',
            'ineffective',
            'no_effect',
            'resistance',
            'super_effective',
            'weakness'
        )

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class MoveResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Move'
        resource_name = 'move'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'name',
            'id',
            'created',
            'modified',
            'description',
            'power',
            'accuracy',
            'category',
            'pp'
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
            'name',
            'id',
            'created',
            'modified',
            'description'
        )

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class EggResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Egg'
        resource_name = 'egg'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'name',
            'id',
            'created',
            'modified',
            'pokemon'
        )

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class DescriptionResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Description'
        resource_name = 'description'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'name',
            'id',
            'created',
            'modified',
            'games',
            'pokemon',
            'description'
        )

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class SpriteResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Sprite'
        resource_name = 'sprite'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'name',
            'id',
            'created',
            'modified',
            'pokemon',
            'image'
        )

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())


class GameResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Game'
        resource_name = 'game'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'name',
            'id',
            'created',
            'modified',
            'release_year',
            'generation'
        )

    def __repr__(self):
        return '<%s - %s>' % (self.Meta.name, self.name.capitalize())
