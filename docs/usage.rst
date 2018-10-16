========
Usage
========

To use Pykemon in a project::

    >>> import pykemon

======
API
======

Since version 0.2.0, Pykemon now works with `Beckett <https://phalt.github.io/beckett>`_, an easy to use API Client Framework::

   >>> client = pykemon.V2Client()
   >>> bulba = client.get_pokemon(1)[0]
   <Pokemon - Bulbasaur>
   >>> bulba.name
   Bulbasaur

The following methods work with the V2 client and all take a `uid` parameter:

* get_berry
* get_berry_firmness
* get_berry_flavor
* get_contest_type
* get_contest_effect
* get_super_contest_effect
* get_encounter_method
* get_encounter_condition
* get_encounter_condition_value
* get_evolution_chain
* get_evolution_trigger
* get_generation
* get_pokedex
* get_version
* get_version_group
* get_item
* get_item_attribute
* get_item_category
* get_item_fling_effect
* get_item_pocket
* get_machine
* get_move
* get_move_ailment
* get_move_battle_style
* get_move_category
* get_move_damage_class
* get_move_learn_method
* get_move_target
* get_location
* get_location_area
* get_pal_park_area
* get_region
* get_ability
* get_characteristic
* get_egg_group
* get_gender
* get_growth_rate
* get_nature
* get_pokeathlon_stat
* get_pokemon
* get_pokemon_color
* get_pokemon_form
* get_pokemon_habitat
* get_pokemon_shape
* get_pokemon_species
* get_stat
* get_type
* get_language

Please refer to the pokeapi documentation (https://pokeapi.co/docs/v2.html/) for more information on what each of these methods returns

Then you can start grabbing stuff from the API::

    >>> pykemon.V2Client().get_pokemon('mew')[0]
    <Pokemon - Mew>
    >>> pykemon.V2Client().get_pokemon(1)[0]
    <Pokemon - Bulbasaur>
    >>> pykemon.V2Client().get_move(15)[0]
    <Move - Cut>
    >>> pykemon.V2Client().get_ability(15)[0]
    <Ability - stench>

Resources that have other abilities linked are displayed as dicts::

    >>> p = pykemon.V2Client().get_pokemon(1)[0]
    >>> p
    <Pokemon - Bulbasaur>
    >>> p.types
    [{u'slot': 2, u'type': {u'url': u'https://pokeapi.co/api/v2/type/4/', u'name': u'poison'}}, {u'slot': 1, u'type': {u'url': u'https://pokeapi.co/api/v2/type/12/', u'name': u'grass'}}]


With the resource uri information you can request the linked resources easily.

==========
Options
==========

Most resources can be requested by using either the name or id::

    >>> pykemon.V2Client().get_pokemon('rotom')[0]
    <Pokemon - Rotom>
    >>> pykemon.V2Client().get_pokemon(479)[0]
    <Pokemon - Rotom>

Make sure you use lower case strings!
