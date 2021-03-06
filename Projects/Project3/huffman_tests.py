import unittest
import filecmp
import subprocess
from huffman import *

class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist	= cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist)

    def test_02_cnt_freq(self):
        with self.assertRaises(FileNotFoundError):
            cnt_freq("file9.txt")

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_03_textfile(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_07_textfile(self):
        with self.assertRaises(FileNotFoundError):
            huffman_decode("Jimmy", "James")

    def test_08_textfile(self):
        huffman_decode("spam_out.txt", "spam_test.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb spam_test.txt spam.txt", shell = True)
        self.assertEqual(err, 0)

    def test_09_textfile(self):
        huffman_decode("zero_out.txt", "zero_test.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb zero_test.txt zero.txt", shell = True)
        self.assertEqual(err, 0)

    def test_06_textfile(self):
        huffman_decode("declaration_out.txt", "declaration_decode.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declaration_decode.txt declaration.txt", shell = True)
        self.assertEqual(err, 0)


if __name__ == '__main__': 
   unittest.main()
