===============================
Pykemon
===============================

.. image:: https://badge.fury.io/py/pykemon.png
    :target: http://badge.fury.io/py/pykemon

.. image:: https://circleci.com/gh/PokeAPI/pykemon.svg?style=svg
    :target: https://circleci.com/gh/PokeAPI/pykemon

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
    >>> client = pykemon.V1Client()
    >>> client.get_pokemon(uid=1)
    [<Pokemon - Bulbasaur>]


Features
--------

* Generate Python objects from PokeAPI resources.

* Human-friendly API
