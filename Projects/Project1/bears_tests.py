import unittest
import bears

class TestAssign1(unittest.TestCase):
    def test_bear_01(self):
        self.assertTrue(bears.bears(250))

    def test_bear_02(self):
        self.assertTrue(bears.bears(42))

    def test_bear_03(self):
        self.assertFalse(bears.bears(53))

    def test_bear_04(self):
        self.assertFalse(bears.bears(41))

if __name__ == "__main__":
    unittest.main()
