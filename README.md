# Pokepy <a href="https://pokeapi.co/api/v2/pokemon/kakuna"><img src='https://veekun.com/dex/media/pokemon/global-link/14.png' height=50px/></a>

[![pypi](https://img.shields.io/pypi/v/pokepy.svg "pypi package")](https://pypi.org/project/pokepy)
[![python versions](https://img.shields.io/pypi/pyversions/pokepy.svg "supported python versions")](https://pypi.org/project/pokepy)
[![downloads](https://img.shields.io/pypi/dm/pokepy.svg?style=popout "pypi downloads")](https://pypi.org/project/pokepy/)
[![build status](https://circleci.com/gh/PokeAPI/pokepy.svg?style=svg "build status")](https://circleci.com/gh/PokeAPI/pokepy)
[![coverage](https://codecov.io/gh/PokeAPI/pokepy/branch/master/graph/badge.svg "code coverage")](https://codecov.io/gh/PokeAPI/pokepy)
[![snyk](https://snyk.io/test/github/PokeAPI/pokepy/badge.svg?targetFile=requirements.txt "known vulnerabilities")](https://snyk.io/test/github/PokeAPI/pokepy?targetFile=requirements.txt)
[![license](https://img.shields.io/pypi/l/pokepy.svg "license")](https://github.com/PokeAPI/pokepy/blob/master/LICENSE)

A python wrapper for [PokéAPI](https://pokeapi.co). (former [pykemon](https://github.com/PokeAPI/pokepy/tree/bb72105f4c5402aaa5d4fd2b9c142bf9b678b254))

Maintainer: [Kronopt](https://github.com/Kronopt)

## Installation

Nice and simple:

```sh
$ pip install pokepy
```

## Usage

Even simpler:

```python
>>> import pokepy
>>> client = pokepy.V2Client()
>>> client.get_pokemon(14)
<Pokemon - Kakuna>
```

## Documentation

For more information, check the documentation at https://pokeapi.github.io/pokepy

## Features

* Generate Python objects from PokéAPI resources
* Cache
* Human-friendly API
