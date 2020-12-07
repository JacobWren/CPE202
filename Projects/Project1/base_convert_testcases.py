import unittest
from Projects.Project1 import base_convert


class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(base_convert.convert(45, 2), "101101")

    def test_base4(self):
        self.assertEqual(base_convert.convert(30, 4), "132")

    def test_base16(self):
        self.assertEqual(base_convert.convert(316, 16), "13C")

    def test_base17(self):
        self.assertEqual(base_convert.convert(316, 17), "11A")

    def test_base13(self):
        self.assertEqual(base_convert.convert(316, 13), "1B4")

    def test_base43(self):
        self.assertEqual(base_convert.convert(316, 43), "7F")

    def test_base14(self):
        self.assertEqual(base_convert.convert(379, 14), "1D1")

    def test_base15(self):
        self.assertEqual(base_convert.convert(389, 15), "1AE")

    def test_base10(self):
        self.assertEqual(base_convert.convert(0, 10), str(0))

    def test_base16_2(self):
        self.assertEqual(base_convert.convert(11259375, 16), "ABCDEF")

if __name__ == "__main__":
        unittest.main()