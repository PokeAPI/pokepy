#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pykemon
----------------------------------

Tests for `pykemon` module.
"""

import unittest

from pykemon import pykemon


class TestPykemon(unittest.TestCase):

    def setUp(self):
        self.poke_one = pykemon.get(pokemon='bulbasaur')
        self.poke_1 = pykemon.get(pokemon_id=1)
        self.poke_two = pykemon.get(pokemon='mew')
        self.poke_fail = pykemon.get(pokemon='gibberish')
        self.poke_fail_2 = pykemon.get()

    def test_attributes(self):
        assert 1 = 1

if __name__ == '__main__':
    unittest.main()
