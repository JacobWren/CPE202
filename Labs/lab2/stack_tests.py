import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
#from stack_array import Stack
from stack_linked import *

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)

    def test_simple2(self):
        stack = Stack(5)
        stack.push(0)
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.pop()
        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_simple3(self):
        stack = Stack(5)
        stack.push(0)
        stack.pop()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_simple4(self):
        stack = Stack(3)
        stack.push(0)
        stack.push(0)
        stack.push(0)
        with self.assertRaises(IndexError):
            stack.push(0)

    def test_simple5(self):
        stack = Stack(5)
        stack.push(0)
        stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_simple6(self):
        stack = Stack(5)
        stack.push(0)
        stack.push(0)
        stack.push(0)
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_simple7(self):
        stack = Stack(4)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.peek(), 4)
        self.assertTrue(stack.is_full())

    def test_simple8(self):
        stack = Stack(3)
        stack.push(0)
        stack.push(1)
        self.assertEqual(stack.pop(), 1)
        stack.push(9)
        self.assertEqual(stack.pop(), 9)
        stack.pop()
        stack.push(5)
        self.assertEqual(stack.pop(), 5)

    def test_simple9(self):
        stack = Stack(3)
        stack.push(0)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), 0)


if __name__ == '__main__': 
    unittest.main()
