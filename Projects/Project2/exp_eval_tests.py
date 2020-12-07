# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_012(self):
        self.assertAlmostEqual(postfix_eval("2 3 2 ** *"), 18)

    def test_postfix_eval_013(self):
        self.assertAlmostEqual(postfix_eval("2 3 >>"), 0)

    def test_postfix_eval_014(self):
        self.assertAlmostEqual(postfix_eval("2 3 <<"), 16)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_02(self):
        try:
            postfix_eval("3 5 +.")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        with self.assertRaises(ValueError):
            postfix_eval("20 2 / 5 + 12 2 / 6 - / 3 +")

    def test_postfix_eval_06(self):
        try:
            postfix_eval("10.2 11 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")


    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
        self.assertEqual(infix_to_postfix("3 << 4 ** 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 << 2 ** 1 5 - 2 3 ** ** /")


    def test_prefix_to_postfix(self):
       self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

if __name__ == "__main__":
    unittest.main()
