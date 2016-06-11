========
Usage
========

To use Pykemon in a project::

>>> import pykemon

=======
New API
=======

Since version 0.2.0, Pykemon now works with `Beckett <https://phalt.github.io/beckett>`_, an easy to use API Client Framework::

   >>> client = pykemon.V1Client()
   >>> bulba = client.get_pokemon(uid=1)[0]
   <Pokemon | Bulbasaur>
   >>> bulba.name
   Bulbasaur

The following methods work with this client and all take a `uid` parameter:

* get_pokemon
* get_move
* get_sprite
* get_ability
* get_game
* get_type
* get_egg


================
Version 0.1* API
================

Then you can start grabbing stuff from the API::

    >>> pykemon.get(pokemon='mew')
    <Pokemon - Mew>
    >>> pykemon.get(pokemon_id=1)
    <Pokemon - Bulbasaur>

Fully supports all the resources on PokeAPI::

    >>> pykemon.get(move_id=15)
    <Move - Cut>
    >>> pykemon.get(ability_id=1)
    <Ability - stench>

Resources that have other abilities linked are displayed as dicts::

    >>> p = pykemon.get(pokemon_id=1)
    >>> p
    <Pokemon - Bulbasaur>
    >>> p.evolutions
    {'Ivysaur': '/api/v1/pokemon/2/'}

With the resource uri information you can request the linked resources easily.


=====
Options
====

Each resource is accessible, with it's own object-oriented representation.
Every resource can be accessed with the term::

    resource_id

Where 'resource' is replaced depending on the resource you want::

    pokemon_id
    move_id
    ability_id
    egg_id
    type_id
    description_id
    game_id
    sprite_id

The Pokemon resource can also be requested using the name:

    >>> pykemon.get(pokemon='rotom')
    <Pokemon - Rotom>

Make sure you use lower case strings!
