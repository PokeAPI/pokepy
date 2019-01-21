========
Usage
========

To use Pokepy in a project::

    >>> import pokepy

======
API
======

Since version 0.2.0, Pokepy now works with `Beckett <https://phalt.github.io/beckett>`_, an easy to use API Client Framework::

   >>> client = pokepy.V2Client()
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

    >>> pokepy.V2Client().get_pokemon('mew')[0]
    <Pokemon - Mew>
    >>> pokepy.V2Client().get_pokemon(1)[0]
    <Pokemon - Bulbasaur>
    >>> pokepy.V2Client().get_move(15)[0]
    <Move - Cut>
    >>> pokepy.V2Client().get_ability(15)[0]
    <Ability - stench>

Resources that have other abilities linked are displayed as dicts::

    >>> p = pokepy.V2Client().get_pokemon(1)[0]
    >>> p
    <Pokemon - Bulbasaur>
    >>> p.types
    [{u'slot': 2, u'type': {u'url': u'https://pokeapi.co/api/v2/type/4/', u'name': u'poison'}}, {u'slot': 1, u'type': {u'url': u'https://pokeapi.co/api/v2/type/12/', u'name': u'grass'}}]


With the resource uri information you can request the linked resources easily.

==========
Options
==========

Most resources can be requested by using either the name or id::

    >>> pokepy.V2Client().get_pokemon('rotom')[0]
    <Pokemon - Rotom>
    >>> pokepy.V2Client().get_pokemon(479)[0]
    <Pokemon - Rotom>

Make sure you use lower case strings!

========
Cache
========

If you use the API to get the same resources often, you can enable cache to avoid overloading the pokeapi server.
You can either enable `in-memory` or `in-disk` cache.
Cache is kept per get method.

`in-memory` cache saves resources in RAM::

    >>> client = pokepy.V2Client(cache='in_memory')

To check the state of the cache of a particular method::

    >>> client.get_pokemon(1)
    >>> client.get_pokemon.cache_info()
    CacheInfo(hits=0, misses=1, size=1)

Calling the same resource as before will retrieve the resource from the cache::

    >>> client.get_pokemon(1)
    >>> client.get_pokemon.cache_info()
    CacheInfo(hits=1, misses=1, size=1)

To clear the cache::

    >>> client.get_pokemon.cache_clear()
    >>> client.get_pokemon.cache_info()
    CacheInfo(hits=0, misses=0, size=0)

`in-disk` cache saves resources to the disk. Cache is kept per get method::

    >>> pokepy.V2Client(cache='in_disk', cache_location='/temp')

The same methods are used as with `in-memory` to check the state and clear the cache.
You can also check the cache directory::

    >>> client.get_pokemon.cache_location()
    /temp

Disk-based cache is reloaded automatically between runs if the same cache directory is specified.
