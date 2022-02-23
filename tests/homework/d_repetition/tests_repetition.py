import unittest

from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers
#from src.homework.d_repetition.repetition import sum_odd_numbers

class Test_Config(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(get_factorial(5), 120)

    def test_sum_odd_numbers(self):
        self.assertEqual(sum_odd_numbers(8), 16)