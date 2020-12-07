import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())

    def test_09(self):
        g = Graph('mytest.txt')
        self.assertEqual(g.conn_components(), [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'S']])
        self.assertTrue(g.is_bipartite())
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    def test_03(self):
        g = Graph('ttest.txt')
        self.assertEqual(g.conn_components(), [['A','B','C']])
        self.assertFalse(g.is_bipartite())

    def test_04(self):
        g = Graph('test3.txt')
        self.assertEqual(g.conn_components(), [['V1', 'V2', 'V3','V4','V5']])
        self.assertFalse(g.is_bipartite())

    def test_05(self):
        g = Graph('test4.txt')
        self.assertEqual(g.conn_components(), [['v0', 'v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())

if __name__ == '__main__':
   unittest.main()
