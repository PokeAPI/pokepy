#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pykemon
----------------------------------

Tests for `pykemon` module.
"""

import unittest

from pykemon import Pokemon


class TestPykemon(unittest.TestCase):

    def setUp(self):
        self.poke_one = Pokemon('bulbasaur')
        self.poke_1 = Pokemon(id=1)
        self.poke_two = Pokemon('mew')
        self.poke_fail = Pokemon('gibberish')
        self.poke_fail_2 = Pokemon()

    def test_attributes(self):
        pass

if __name__ == '__main__':
    unittest.main()
