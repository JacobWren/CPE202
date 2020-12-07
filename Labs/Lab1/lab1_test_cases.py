import unittest
import lab1

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """test max_list_iter function. Edge cases include empty lists and lists of length 1"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            lab1.max_list_iter(tlist)
        self.assertEqual(lab1.max_list_iter([]), None)
        self.assertEqual(lab1.max_list_iter([1]), 1)
        self.assertEqual(lab1.max_list_iter([1, 2]), 2)
        self.assertEqual(lab1.max_list_iter([2, 1]), 2)
        self.assertEqual(lab1.max_list_iter([1, 2, 3]), 3)
        self.assertEqual(lab1.max_list_iter([1, 3, 2]), 3)

    def test_reverse_rec(self):
        """test reverse_rec function. Edge cases include empty lists and lists of length 1"""
        with self.assertRaises(ValueError):
            lab1.reverse_rec(None)
        self.assertEqual(lab1.reverse_rec([]),[])
        self.assertEqual(lab1.reverse_rec([1]), [1])
        self.assertEqual(lab1.reverse_rec([1,2,3]),[3,2,1])

    def test_bin_search(self):
        """test bin_searc function. Edge cases include empty lists, lists of length 1, and cases
            where the target value is not found"""
        with self.assertRaises(ValueError):
            lab1.bin_search(1, 0, 0, None)
        self.assertEqual(lab1.bin_search(1, 0, 0, []), None)
        self.assertEqual(lab1.bin_search(1, 0, 0, [1]), 0)
        self.assertEqual(lab1.bin_search(2, 0, 0, [1]), None)
        x = list(range(2, 50000, 2))
        for i in range(1, 50000, 2):
            self.assertEqual(lab1.bin_search(i, 0, 2498, x), None)
        self.assertEqual(lab1.bin_search(3, 0, 4, [1, 2, 3, 4, 5]), 2)
        self.assertEqual(lab1.bin_search(4, 0, 4, [1, 2, 3, 4, 5]), 3)
        self.assertEqual(lab1.bin_search(2, 0, 4, [1, 2, 3, 4, 5]), 1)
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(lab1.bin_search(4, 0, len(list_val)-1, list_val), 4 )

if __name__ == "__main__":
        unittest.main()

    
