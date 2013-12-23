===============================
Pykemon
===============================

.. image:: https://badge.fury.io/py/pykemon.png
    :target: http://badge.fury.io/py/pykemon

.. image:: https://travis-ci.org/phalt/pykemon.png?branch=master
        :target: https://travis-ci.org/phalt/pykemon

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
    >>> pykemon.get(move_id=15)
    <Move - cut>


Features
--------

* Generate Python objects from PokeAPI resources.

* Human-friendly API
