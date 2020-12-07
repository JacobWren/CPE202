import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_num_items(), 0)

    def test_01c(self):
        ht = HashTable(7)
        self.assertAlmostEqual(ht.get_load_factor(), 0)

    def test_01d(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_all_keys(), [])

    def test_01e(self):
        ht = HashTable(7)
        self.assertEqual(ht.in_table("cat"), False)

    def test_01ef(self):
        ht = HashTable(7)
        ht.insert("dog", 5)
        self.assertEqual(ht.in_table("cat"), False)

    def test_01f(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_value("cat"), None)

    def test_01g(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_index("cat"), None)

    def test_01h(self):
        ht = HashTable(7)
        self.assertEqual(ht.horner_hash("cat"), 3)

    def test_02a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_02b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_02c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_02cd(self):
        ht = HashTable(2)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1 / 2)
        ht.insert("bird", 6)
        ht.insert("bat", 6)

    def test_02d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_02e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_02f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), [5])

    def test_02g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_03(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("cat", 17)
        self.assertEqual(ht.get_value("cat"), [5, 17])

    def test_04(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

        ht.insert("dog", 8)
        self.assertEqual(ht.get_num_items(), 2)
        self.assertEqual(ht.get_index("dog"), 6)
        self.assertAlmostEqual(ht.get_load_factor(), 2 / 7)

        ht.insert("mouse", 10)
        self.assertEqual(ht.get_num_items(), 3)
        self.assertEqual(ht.get_index("mouse"), 4)
        self.assertAlmostEqual(ht.get_load_factor(), 3 / 7)

        ht.insert("elephant", 12) # hash table should be resized
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_table_size(), 15)
        self.assertAlmostEqual(ht.get_load_factor(), 4 / 15)
        self.assertEqual(ht.get_index("cat"), 12)
        self.assertEqual(ht.get_index("dog"), 14)
        self.assertEqual(ht.get_index("mouse"), 13)
        self.assertEqual(ht.get_index("elephant"), 9)
        keys = ht.get_all_keys()
        keys.sort()
        self.assertEqual(keys, ["cat", "dog", "elephant", "mouse"])

    def test_04(self):
        ht = HashTable(5)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("dog"), None)

    def test_05(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("dog", 4)
        ht.insert("pig", 3)
        self.assertEqual(ht.get_value("deer"), None)

    def test_06(self):
        ht = HashTable(3)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1 / 3)
        ht.insert("dino", 6)

    def test_07(self):
        ht = HashTable(9)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1 / 9)
        ht.insert("dino", 6)
        ht.insert("Jim", 7)
        ht.insert("Rex", 8)

    def test_08(self):
        ht = HashTable(9)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1 / 9)
        ht.insert("dino", 6)
        ht.insert("Jim", 7)
        ht.insert("Rex", 8)
        ht.insert("Jim", 5)
        self.assertEqual(ht.in_table("dino"), True)
        self.assertEqual(ht.in_table("flip"), False)
        self.assertEqual(ht.in_table("Rex"), True)
        self.assertEqual(ht.in_table("Batman"), False)
        self.assertEqual(ht.get_index("dino"), 1)
        self.assertEqual(ht.in_table("JIMBO"), False)

    def test_09(self):
        ht = HashTable(9)
        ht.insert("cat", 5)
        ht.insert("cat", 17)
        ht.insert("dino", 6)
        ht.insert("Jim", 7)
        ht.insert("Rex", 8)
        ht.insert("Jim", 5)
        self.assertEqual(ht.get_value("cat"), [5, 17])
        self.assertEqual(ht.get_value("Jim"), [7, 5])
        self.assertEqual(ht.get_value("dino"), [6])
        self.assertEqual(ht.get_value("dim"), None)
        self.assertEqual(ht.in_table("cat"), True)
        self.assertEqual(ht.get_index("Jim"), 3)
        self.assertEqual(ht.get_index("Rex"), 4)
        self.assertEqual(ht.get_index("cat"), 0)

    def test_10(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("chimp"), None)

    def test_11(self):
        ht = HashTable(9)
        ht.insert("cat", 5)
        ht.insert("cat", 17)
        ht.insert("dino", 6)
        ht.insert("Jim", 7)
        ht.insert("Rex", 8)
        ht.insert("Jim", 5)
        ht.insert("cat", 1)
        self.assertEqual(ht.in_table("mike"), False)

    def test_12(self):
        ht = HashTable(9)
        ht.insert("cat", 5)
        ht.insert("cat", 17)
        ht.insert("dino", 6)
        ht.insert("Jim", 7)
        ht.insert("Rex", 8)
        ht.insert("cat", 16)
        ht.insert("Jim", 5)
        ht.insert("cat", 19)
        self.assertEqual(ht.get_value("Jim"), [7, 5])

    def test_13(self):
        ht = HashTable(9)
        ht.insert("cat", 5)
        ht.insert("cd", 6)
        ht.insert("cr", 6)
        ht.insert("cat", 17)
        ht.insert("cc", 6)
        ht.insert("dino", 6)
        ht.insert("Jim", 7)
        ht.insert("Rex", 8)
        ht.insert("cat", 16)
        ht.insert("ccc", 6)
        ht.insert("ct", 6)
        ht.insert("cq", 6)
        ht.insert("cw", 6)
        ht.insert("cy", 6)
        ht.insert("Jim", 5)
        ht.insert("cat", 19)
        ht.insert("cz", 6)
        ht.insert("cv", 6)

    def test_14(self):
        ht = HashTable(8)
        ht.insert("cat", 5)
        ht.insert("dino", 5)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), [5])

    def test_15(self):
        ht = HashTable(3)
        ht.insert("cat", 9)
        ht.insert("dog", 10)
        ht.insert("dino", 90)
        ht.insert("deer", 1)
        self.assertEqual(ht.in_table("deer"), True)

    def test_18(self):
        ht = HashTable(3)
        ht.insert("cat", 5)
        ht.insert("cat", 17)
        ht.insert("cat", 4)
        ht.insert("cat", 6)
        ht.insert("cat", 8)
        self.assertEqual(ht.get_num_items(), 1)
        self.assertEqual(ht.get_table_size(), 3)

    def test_17(self):
        ht = HashTable(9)
        ht.insert("cbQ", 6)
        ht.insert("cap", 7)
        ht.insert("m", 6)
        ht.insert("cbQ", 6)
        ht.insert("cap", 7)
        ht.insert("m", 6)
        ht.get_value("cbQ")
        ht.get_value("capo")

    def test_19(self):
        ht = HashTable(3)
        ht.insert("cat", 9)
        ht.insert("dog", 10)
        ht.insert("dino", 90)
        ht.insert("cat", 9)
        ht.insert("dog", 10)
        ht.insert("dino", 90)
        self.assertEqual(ht.get_value("cat"), [9])


if __name__ == '__main__':
   unittest.main()
