import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_simple_2(self):
        O = OrderedList()
        O.add(0)
        O.add(0)
        O.add(1)
        O.add(1)
        O.add(2)
        O.add(2)
        self.assertFalse(O.is_empty())
        self.assertTrue(O.remove(0))
        self.assertTrue(O.remove(1))
        self.assertTrue(O.remove(2))
        self.assertTrue(O.is_empty())
        self.assertEqual(O.python_list(), [])
        self.assertEqual(O.index(2), None)
        with self.assertRaises(IndexError):
            O.pop(1)
        O.add(2)
        with self.assertRaises(IndexError):
            O.pop(1)
        O.add(1)
        O.add(3)
        with self.assertRaises(IndexError):
            O.pop(4)
        self.assertEqual(O.index(0), None)
        self.assertEqual(O.index(1), 0)
        self.assertEqual(O.index(2), 1)
        self.assertEqual(O.index(3), 2)
        self.assertEqual(O.pop(0), 1)
        self.assertEqual(O.pop(1), 3)
        self.assertEqual(O.pop(0), 2)
        self.assertTrue(O.is_empty())
        self.assertFalse(O.remove(1))
        O.add(3)
        self.assertFalse(O.remove(1))
        self.assertEqual(O.index(2), None)
        with self.assertRaises(IndexError):
            O.pop(-1)
        O.add(0)
        O.add(1)
        O.add(2)
        self.assertTrue(O.search(0))
        self.assertTrue(O.search(1))
        self.assertTrue(O.search(2))
        self.assertFalse(O.search(4))
        self.assertEqual(O.python_list(), [0, 1, 2, 3])
        self.assertEqual(O.python_list_reversed(), [3, 2, 1, 0])
        self.assertEqual(O.size(), 4)
        self.assertTrue(O.remove(2))
        self.assertTrue(O.remove(1))

    def test_simple_3(self):
        OL = OrderedList()
        OL.add(2)
        OL.add(3)
        OL.add(1)
        OL.add(1)
        OL.add(4)
        self.assertTrue(OL.remove(4))
        self.assertFalse(OL.remove(5))


if __name__ == '__main__': 
    unittest.main()
