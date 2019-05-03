# Usage
To use Pokepy in a project:
```python
>>> import pokepy
```

### API
Pokepy is composed of a single class, `V2Client`, which implements the whole 
[v2 PokéAPI](https://pokeapi.co/docs/v2.html).
This class is usually instantiated without parameters:
```python
>>> client = pokepy.V2Client()
```
Unless you want to use the caching feature, which is discussed [further below](#cache).

Each endpoint of PokéAPI is represented in `V2Client` by a `get_<endpoint_name>` method,
all taking a single parameter (`uid`), which can be either an `integer` (for most endpoints) or a `string`.

The following is an exhaustive list of all the endpoints with links to their respective PokéAPI documentation:

* [get_berry](https://pokeapi.co/docs/v2.html/#berries)
* [get_berry_firmness](https://pokeapi.co/docs/v2.html/#berry-firmnesses)
* [get_berry_flavor](https://pokeapi.co/docs/v2.html/#berry-flavors)
* [get_contest_type](https://pokeapi.co/docs/v2.html/#contest-types)
* [get_contest_effect](https://pokeapi.co/docs/v2.html/#contest-effects)
* [get_super_contest_effect](https://pokeapi.co/docs/v2.html/#super-contest-effects)
* [get_encounter_method](https://pokeapi.co/docs/v2.html/#encounter-methods)
* [get_encounter_condition](https://pokeapi.co/docs/v2.html/#encounter-conditions)
* [get_encounter_condition_value](https://pokeapi.co/docs/v2.html/#encounter-condition-values)
* [get_evolution_chain](https://pokeapi.co/docs/v2.html/#evolution-chains)
* [get_evolution_trigger](https://pokeapi.co/docs/v2.html/#evolution-triggers)
* [get_generation](https://pokeapi.co/docs/v2.html/#generations)
* [get_pokedex](https://pokeapi.co/docs/v2.html/#pokedexes)
* [get_version](https://pokeapi.co/docs/v2.html/#version)
* [get_version_group](https://pokeapi.co/docs/v2.html/#version-groups)
* [get_item](https://pokeapi.co/docs/v2.html/#item)
* [get_item_attribute](https://pokeapi.co/docs/v2.html/#item-attributes)
* [get_item_category](https://pokeapi.co/docs/v2.html/#item-categories)
* [get_item_fling_effect](https://pokeapi.co/docs/v2.html/#item-fling-effects)
* [get_item_pocket](https://pokeapi.co/docs/v2.html/#item-pockets)
* [get_location](https://pokeapi.co/docs/v2.html/#locations)
* [get_location_area](https://pokeapi.co/docs/v2.html/#location-areas)
* [get_pal_park_area](https://pokeapi.co/docs/v2.html/#pal-park-areas)
* [get_region](https://pokeapi.co/docs/v2.html/#regions)
* [get_machine](https://pokeapi.co/docs/v2.html/#machines)
* [get_move](https://pokeapi.co/docs/v2.html/#moves)
* [get_move_ailment](https://pokeapi.co/docs/v2.html/#move-ailments)
* [get_move_battle_style](https://pokeapi.co/docs/v2.html/#move-battle-styles)
* [get_move_category](https://pokeapi.co/docs/v2.html/#move-categories)
* [get_move_damage_class](https://pokeapi.co/docs/v2.html/#move-damage-classes)
* [get_move_learn_method](https://pokeapi.co/docs/v2.html/#move-learn-methods)
* [get_move_target](https://pokeapi.co/docs/v2.html/#move-targets)
* [get_ability](https://pokeapi.co/docs/v2.html/#abilities)
* [get_characteristic](https://pokeapi.co/docs/v2.html/#characteristics)
* [get_egg_group](https://pokeapi.co/docs/v2.html/#egg-groups)
* [get_gender](https://pokeapi.co/docs/v2.html/#genders)
* [get_growth_rate](https://pokeapi.co/docs/v2.html/#growth-rates)
* [get_nature](https://pokeapi.co/docs/v2.html/#natures)
* [get_pokeathlon_stat](https://pokeapi.co/docs/v2.html/#pokeathlon-stats)
* [get_pokemon](https://pokeapi.co/docs/v2.html/#pokemon)
* [get_pokemon_color](https://pokeapi.co/docs/v2.html/#pok%C3%A9mon-colors)
* [get_pokemon_form](https://pokeapi.co/docs/v2.html/#pok%C3%A9mon-forms)
* [get_pokemon_habitat](https://pokeapi.co/docs/v2.html/#pok%C3%A9mon-habitats)
* [get_pokemon_shape](https://pokeapi.co/docs/v2.html/#pok%C3%A9mon-shapes)
* [get_pokemon_species](https://pokeapi.co/docs/v2.html/#pok%C3%A9mon-species)
* [get_stat](https://pokeapi.co/docs/v2.html/#stats)
* [get_type](https://pokeapi.co/docs/v2.html/#types)
* [get_language](https://pokeapi.co/docs/v2.html/#languages)

Each method returns an object containing as many python attributes as there are named attributes.
Please refer to the [PokéAPI documentation](https://pokeapi.co/docs/v2.html/)
for more information on what each of these methods returns, its description and type.

Then you can start grabbing stuff from the API:
```python
>>> mew = pokepy.V2Client().get_pokemon('mew')
>>> mew
<Pokemon - Mew>
>>> mew.name
mew
```

```python
>>> kakuna = pokepy.V2Client().get_pokemon(14)
>>> kakuna
<Pokemon - Kakuna>
>>> kakuna.weigth
100
```

```python
>>> cut = pokepy.V2Client().get_move(15)
>>> cut
<Move - Cut>
>>> cut.power
50
```

Some resources have subresources:

```python
>>> kakuna = pokepy.V2Client().get_pokemon(14)
>>> kakuna
<Pokemon - Kakuna>
>>> kakuna.types
[<Pokemon_Type>, <Pokemon_Type>]
>>> kakuna.types[0].type.name
poison
```

```python
>>> insomnia = pokepy.V2Client().get_ability(15)
>>> insomnia
<Ability - Insomnia>
>>> insomnia.effect_entries[0].short_effect
Prevents sleep.
```

### Parameters
Most resources can be requested by using either the `name` or `id` of the resource:
```python
>>> pokepy.V2Client().get_pokemon('rotom')
<Pokemon - Rotom>
>>> pokepy.V2Client().get_pokemon(479)
<Pokemon - Rotom>
>>> pokepy.V2Client().get_pokemon('479')
<Pokemon - Rotom>
```

### Cache
If you use the API to get the same resources often,
you can enable cache to avoid making unnecessary requests to the PokéAPI server.
You can either enable `memory-based` or `disk-based` cache.

#### Memory-based
Memory-based cache is activated by passing `in_memory` to the `cache` parameter of `V2Client`.
Resources obtained from the PokéAPI are then saved in RAM. Cache is kept per get method:
```python
>>> client_mem_cache = pokepy.V2Client(cache='in_memory')
```

You can check the state of the cache in two ways: per get method or as a whole.

To check the state of the cache of a particular method, call the `cache_info()`
of that get method:
```python
>>> client_mem_cache.get_pokemon.cache_info()
CacheInfo(hits=0, misses=0, size=0)
```

To check the state of the cache as a whole (all get methods combined),
call the `cache_info()` of `V2Client`:
```python
>>> client_mem_cache.cache_info()
CacheInfo(hits=0, misses=0, size=0)
```

`hits` is the number of previously cached parametes which were returned,
`misses` is the number given parameters not previously cached (which are now cached),
and `size` is the total number of cached parameters.

When calling a certain endpoint, the `cache_info` reflects that call:
```python
>>> kakuna = client_mem_cache.get_pokemon(14)
>>> client_mem_cache.get_pokemon.cache_info()
CacheInfo(hits=0, misses=1, size=1)
```

Calling the same resource as before with the same parameters will retrieve
the cached resource instead of getting it from the server:
```python
>>> kakuna = client_mem_cache.get_pokemon(14)
>>> client_mem_cache.get_pokemon.cache_info()
CacheInfo(hits=1, misses=1, size=1)
```

To clear the cache of a specific get method:
```python
>>> client_mem_cache.get_pokemon.cache_clear()
>>> client_mem_cache.get_pokemon.cache_info()
CacheInfo(hits=0, misses=0, size=0)
```

To clear all cache:
```python
>>> client_mem_cache.cache_clear()
>>> client_mem_cache.cache_info()
CacheInfo(hits=0, misses=0, size=0)
```

#### Disk-based
Disk-based cache is activated by passing `in_disk` to the `cache` parameter of `V2Client`.
Resources obtained from the PokéAPI are then saved to disk. Cache is kept per get method:
```python
>>> client_disk_cache = pokepy.V2Client(cache='in_disk', cache_location='/temp')
```

In this case it's possible to specify the cache directory with the `cache_location` parameter.
A folder named `pokepy_cache` will be created inside the specified directory, where the
cache of each get method will be located.
If no cache directory is specified a system-appropriate cache directory is automatically determined by
[appdirs](https://pypi.org/project/appdirs/).
 
The methods used to check the state and clear the cache are the same as in the memory-based cache,
including the global `V2Client` methods.

You can also check the cache directory, per get method:
```python
>>> client_disk_cache.get_pokemon.cache_location()
/temp/pokepy_cache/39/cache
```

Or check the global cache directory:
```python
>>> client_disk_cache.cache_location()
/temp/pokepy_cache/
```

Disk-based cache is reloaded automatically between runs if the same cache directory is specified.
