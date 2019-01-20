# Pokepy
A python wrapper for [PokeAPI](https://pokeapi.co). (former pykemon)

* Free software: [BSD license](https://github.com/PokeAPI/pokepy/blob/master/LICENSE)
* Documentation: ~~http://pykemon.rtfd.org~~
* Maintainer: [Kronopt](https://github.com/Kronopt)

# Installation
Nice and simple (soon a new pypi page will be created):

```
$ pip install git+https://github.com/PokeAPI/pokepy.git@master
```

# Usage
Even simpler:

```python
>>> import pokepy
>>> client = pokepy.V2Client()
>>> client.get_pokemon(1)[0]
<Pokemon - Bulbasaur>
```

# Features

* Generate Python objects from PokeAPI resources
* Cache
* Human-friendly API