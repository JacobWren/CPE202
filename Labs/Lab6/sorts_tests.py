import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_simple_1(self):
        nums = [7, 8, 5, 4, 9, 2]
        comps = selection_sort(nums)
        self.assertEqual(comps, 15)
        self.assertEqual(nums, [2, 4, 5, 7, 8, 9])

    def test_simple_2(self):
        nums = [5, 8, 1, 3, 9, 6]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [1, 3, 5, 6, 8, 9])

    def test_simple_3(self):
        nums = [3, 1]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [1, 3])

    def test_simple_4(self):
        nums = [1]
        comps = selection_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [1])

if __name__ == '__main__': 
    unittest.main()
