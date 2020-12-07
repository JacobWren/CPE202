import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        self.assertEqual(perm_lex.perm_gen_lex(''), [])
        self.assertEqual(perm_lex.perm_gen_lex('a'), ['a'])
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])
        self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc','acb','bac','bca','cab','cba'])

if __name__ == "__main__":
        unittest.main()

#python -m coverage report -m Conditions.py
#python3 -m coverage run Test_Conditions.py
#python3 Test_Conditions.py
