===============================
Pokepy
===============================

Evolution of `Pykemon <https://github.com/PokeAPI/pokepy/tree/bb72105f4c5402aaa5d4fd2b9c142bf9b678b254>`_

.. image:: https://badge.fury.io/py/pokepy.png
    :target: http://badge.fury.io/py/pokepy

.. image:: https://circleci.com/gh/PokeAPI/pokepy.svg?style=svg
    :target: https://circleci.com/gh/PokeAPI/pokepy

A python wrapper for `PokeAPI <https://pokeapi.co>`_

* Free software: BSD license
* Documentation: https://pokeapi.github.io/pokepy.


Installation
------------

Nice and simple:

.. code-block:: bash

    $ pip install pokepy


Usage
-----

Even simpler:

.. code-block:: python

    >>> import pokepy
    >>> client = pokepy.V2Client()
    >>> client.get_pokemon(1)[0]
    <Pokemon - Bulbasaur>


Features
--------

* Generate Python objects from PokeAPI resources.
* Human-friendly API
