# Usage
To use Pokepy in a project:
```python
>>> import pokepy
```

### API
Pokepy works with [Beckett](https://phalt.github.io/beckett), since version 0.2.0:
```python
>>> client = pokepy.V2Client()
>>> kakuna = client.get_pokemon(14)[0]
<Pokemon - Kakuna>
>>> kakuna.name
Kakuna
```

The following methods are defined for the `V2Client` and all take a single parameter (`uid`):

* get_berry
* get_berry_firmness
* get_berry_flavor
* get_contest_type
* get_contest_effect
* get_super_contest_effect
* get_encounter_method
* get_encounter_condition
* get_encounter_condition_value
* get_evolution_chain
* get_evolution_trigger
* get_generation
* get_pokedex
* get_version
* get_version_group
* get_item
* get_item_attribute
* get_item_category
* get_item_fling_effect
* get_item_pocket
* get_machine
* get_move
* get_move_ailment
* get_move_battle_style
* get_move_category
* get_move_damage_class
* get_move_learn_method
* get_move_target
* get_location
* get_location_area
* get_pal_park_area
* get_region
* get_ability
* get_characteristic
* get_egg_group
* get_gender
* get_growth_rate
* get_nature
* get_pokeathlon_stat
* get_pokemon
* get_pokemon_color
* get_pokemon_form
* get_pokemon_habitat
* get_pokemon_shape
* get_pokemon_species
* get_stat
* get_type
* get_language

Please refer to the [Pokeapi documentation](https://pokeapi.co/docs/v2.html/)
for more information on what each of these methods returns.

Then you can start grabbing stuff from the API:
```python
>>> pokepy.V2Client().get_pokemon('mew')[0]
<Pokemon - Mew>
>>> pokepy.V2Client().get_pokemon(14)[0]
<Pokemon - Kakuna>
>>> pokepy.V2Client().get_move(15)[0]
<Move - Cut>
>>> pokepy.V2Client().get_ability(15)[0]
<Ability - stench>
```

Some resources have subresources:
```python
>>> kakuna = pokepy.V2Client().get_pokemon(1)[0]
>>> kakuna
<Pokemon - Kakuna>
>>> kakuna.types
[<Pokemon_Type>, <Pokemon_Type>]
```

### Options
Most resources can be requested by using either the name or id:
```python
>>> pokepy.V2Client().get_pokemon('rotom')[0]
<Pokemon - Rotom>
>>> pokepy.V2Client().get_pokemon(479)[0]
<Pokemon - Rotom>
```

### Cache
If you use the API to get the same resources often, you can enable cache to avoid making unnecessary requests to the pokeapi server.
You can either enable `in-memory` or `in-disk` cache.
Cache is kept per get method.

#### In-memory
`in-memory` cache saves resources in RAM. Cache is kept per get method:
```python
>>> client = pokepy.V2Client(cache='in_memory')
```

To check the state of the cache of a particular method::
```python
>>> kakuna = client.get_pokemon(14)
>>> kakuna.get_pokemon.cache_info()
CacheInfo(hits=0, misses=1, size=1)
```

Calling the same resource as before will retrieve the resource from the cache:
```python
>>> kakuna = client.get_pokemon(14)
>>> client.get_pokemon.cache_info()
CacheInfo(hits=1, misses=1, size=1)
```

To clear the cache of a specific get method:
```python
>>> client.get_pokemon.cache_clear()
>>> client.get_pokemon.cache_info()
CacheInfo(hits=0, misses=0, size=0)
```

#### In-disk
`in-disk` cache saves resources to the disk. Cache is kept per get method:
```python
>>> client = pokepy.V2Client(cache='in_disk', cache_location='/temp')
```

The same methods are used as with `in-memory` to check the state and clear the cache.
You can also check the cache directory:
```python
>>> client.get_pokemon.cache_location()
/temp
```

Disk-based cache is reloaded automatically between runs if the same cache directory is specified.
