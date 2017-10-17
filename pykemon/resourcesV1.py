# -*- coding: utf-8 -*-

from beckett.resources import BaseResource


class PokemonResource(BaseResource):
    class Meta(BaseResource.Meta):
        name = 'Pokemon'
        resource_name = 'pokemon'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'created',
            'modified',
            'national_id',
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
            'name',
            'sp_atk',
            'sp_def',
            'speed',
            'total',
            'egg_cycles',
            'ev_yield',
            'exp',
            'growth_rate',
            'height',
            'weight',
            'happiness',
            'male_female_ratio',
            'sprites',
        )

    def __repr__(self):
        return '<Pokemon - %s>' % self.name.capitalize()


class MoveResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Move'
        resource_name = 'move'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'created',
            'modified',
            'id',
            'accuracy',
            'category',
            'power',
            'pp',
            'name',
        )

    def __repr__(self):
        return '<Move - %s>' % self.name.capitalize()


class TypeResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Type'
        resource_name = 'type'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'created',
            'modified',
            'id',
            'name',
            'ineffective',
            'resistance',
            'super_effective',
            'weakness',
        )

    def __repr__(self):
        return '<Type - %s>' % self.name.capitalize()


class AbilityResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Ability'
        resource_name = 'ability'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'created',
            'modified',
            'id',
            'name',
            'description',
        )

    def __repr__(self):
        return '<Ability - %s>' % self.name.capitalize()


class EggResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Egg'
        resource_name = 'egg'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'created',
            'modified',
            'id',
            'name',
            'pokemon',
        )

    def __repr__(self):
        return '<Egg - %s>' % self.name.capitalize()


class DescriptionResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Description'
        resource_name = 'description'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'created',
            'modified',
            'id',
            'name',
            'description',
            'pokemon',
            'games',
        )

    def __repr__(self):
        return '<Description - %s>' % self.name.capitalize()


class SpriteResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Sprite'
        resource_name = 'sprite'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'created',
            'modified',
            'id',
            'name',
            'pokemon',
            'image',
        )

    def __repr__(self):
        return '<Sprite - %s>' % self.name.capitalize()


class GameResource(BaseResource):

    class Meta(BaseResource.Meta):
        name = 'Game'
        resource_name = 'game'
        identifier = 'id'
        methods = (
            'get',
        )
        attributes = (
            'created',
            'modified',
            'id',
            'name',
            'generation',
            'release_year',
        )

    def __repr__(self):
        return '<Game - %s>' % self.name.capitalize()
