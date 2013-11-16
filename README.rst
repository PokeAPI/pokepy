===============================
Pykemon
===============================

.. image:: https://badge.fury.io/py/pykemon.png
    :target: http://badge.fury.io/py/pykemon

.. image:: https://travis-ci.org/phalt/pykemon.png?branch=master
        :target: https://travis-ci.org/phalt/pykemon

.. image:: https://pypip.in/d/pykemon/badge.png
        :target: https://crate.io/packages/pykemon?version=latest

A python wrapper for `PokeAPI <http://pokeapi.co>`_

* Free software: BSD license
* Documentation: http://pykemon.rtfd.org.


Installation
------------

Nice and simple:

.. code-block:: bash

    $ pip install pykemon


Usage
-----

Even simpler:

.. code-block:: python

    >>> import pykemon
    >>> pykemon.get(pokemon='bulbasaur')
    <Pokemon - Bulbasaur>
    >>> p = pykemon.get(pokemon_id=1)
    <Pokemon - Bulbasaur>

Interact with resources linked to Pokemon easily:

.. code-block:: python

    >>> p.moves
    ['cut', 'tackle', 'vine whip']
    >>> p.get_move('cut')
    <Move - cut>

Or grab a resource separately:

.. code-block:: python

    >>> pykemon.get(move='cut')
    <Move - cut>


Features
--------

* Generate objects from PokeAPI resources.

* Human-friendly API
