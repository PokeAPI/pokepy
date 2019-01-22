# Pokepy ![Pokepy](/docs/poke.png?raw=true "Pokepy")

[![pypi](https://img.shields.io/pypi/v/pokepy.svg "pypi package")](https://pypi.org/project/pokepy)
[![python versions](https://img.shields.io/pypi/pyversions/pokepy.svg "supported python versions")](https://pypi.org/project/pokepy)
[![build status](https://circleci.com/gh/PokeAPI/pokepy.svg?style=svg "build status")](https://circleci.com/gh/PokeAPI/pokepy)
[![coverage](https://codecov.io/gh/PokeAPI/pokepy/branch/master/graph/badge.svg "code coverage")](https://codecov.io/gh/PokeAPI/pokepy)
[![license](https://img.shields.io/pypi/l/pokepy.svg "license")](https://github.com/PokeAPI/pokepy/blob/master/LICENSE)

A python wrapper for [PokeAPI](https://pokeapi.co). (former [pykemon](https://github.com/PokeAPI/pokepy/tree/bb72105f4c5402aaa5d4fd2b9c142bf9b678b254))

Maintainer: [Kronopt](https://github.com/Kronopt)

# Installation
Nice and simple:

```
$ pip install pokepy
```

# Usage
Even simpler:

```python
>>> import pokepy
>>> client = pokepy.V2Client()
>>> client.get_pokemon(14)[0]
<Pokemon - Kakuna>
```

For more information, check the documentation: https://pokeapi.github.io/pokepy

# Features

* Generate Python objects from PokeAPI resources
* Cache
* Human-friendly API
