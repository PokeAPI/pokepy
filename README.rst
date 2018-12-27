===============================
Pykemon
===============================

.. image:: https://badge.fury.io/py/pykemon.png
    :target: http://badge.fury.io/py/pykemon

.. image:: https://circleci.com/gh/PokeAPI/pykemon.svg?style=svg
    :target: https://circleci.com/gh/PokeAPI/pykemon

A python wrapper for `PokeAPI <https://pokeapi.co>`_

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
    >>> client = pykemon.V2Client()
    >>> client.get_pokemon(1)[0]
    <Pokemon - Bulbasaur>


Features
--------

* Generate Python objects from PokeAPI resources.
* Cache
* Human-friendly API
