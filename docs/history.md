# History
### 0.6.0 (2019-05-3)
* V2Client get methods now return element instead of single element list
* set urllib3 version to >=1.24.3, <1.25 (CVE-2019-11236)
* Support for Python 3.4 and 3.5

### 0.5.2 (2019-03-01)
* Fixed bug that caused pokemon_encounters subresource to not be detected in LocationAreaResource
(thanks to [jachymb](https://github.com/jachymb))

### 0.5.1 (2019-02-16)
* New V2Client cache-related methods:
    * cache_info
    * cache_clear
    * cache_location

### 0.5.0 (2019-01-19)
* Pykemon is now Pokepy!
* Cache (disk- and memory-based)

### 0.4.0 (2018-10-11)
* Removed code from pre-beckett versions
* Removed V1 API support, as it is now deprecated
* Added some tweaks to the beckett package

### 0.3.0 (2017-10-19)
* V2 support added
* Added some missing V1 resources
* Removed files related to API 0.1

### 0.2.0 (2016-06-11)
* Beckett API Client framework added

### 0.1.2 (2014-1-3)
* Sprite attribute added to Pokemon class

### 0.1.1 (2013-12-24)
* Description attribute added to Pokemon class

### 0.1.0 (2013-12-23)
* First release on PyPI
* All PokéAPI resources fully supported and represented in an object-oriented style
* Easy-to-use API: just one method!
