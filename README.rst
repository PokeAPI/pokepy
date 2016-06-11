===============================
Pykemon
===============================

.. image:: https://badge.fury.io/py/pykemon.png
    :target: http://badge.fury.io/py/pykemon

.. image:: https://travis-ci.org/PokeAPI/pykemon.png?branch=master
        :target: https://travis-ci.org/PokeAPI/pykemon

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
    >>> p = client.get_pokemon(uid=1)
    [<Pokemon - Bulbasaur>]


Features
--------

* Generate Python objects from PokeAPI resources.

* Human-friendly API
