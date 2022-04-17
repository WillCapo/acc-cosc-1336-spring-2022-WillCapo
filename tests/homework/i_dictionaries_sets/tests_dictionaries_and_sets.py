from ast import Add
import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory

class Test_Config(unittest.TestCase):

    def test_inventory(self):
        self.assertEqual(add_inventory('balls', 10), {'balls': 10})

    def test_remove_invetory(self):
        self.assertEqual(remove_inventory('B'), {})