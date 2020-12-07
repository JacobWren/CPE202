import unittest
from queue_array import Queue
#from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_queue2(self):
        q = Queue(5)
        q.enqueue(0)
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(),1)

    def test_queue3(self):
        q = Queue(5)
        q.enqueue(0)
        q.enqueue(1)
        q.dequeue()
        q.dequeue()
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_queue4(self):
        q = Queue(5)
        q.enqueue(0)
        self.assertEqual(q.size(), 1)
        q.dequeue()
        self.assertEqual(q.size(), 0)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_queue5(self):
        q = Queue(3)
        q.enqueue(0)
        q.enqueue(0)
        q.enqueue(0)
        self.assertEqual(q.size(), 3)
        with self.assertRaises(IndexError):
            q.enqueue(0)

    def test_queue7(self):
        q = Queue(5)
        q.enqueue(0)
        q.enqueue(0)
        q.enqueue(0)
        q.dequeue()
        q.dequeue()
        q.dequeue()
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_queue8(self):
        q = Queue(4)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual(q.size(), 4)
        self.assertTrue(q.is_full())

    def test_queue9(self):
        q = Queue(5)
        q.enqueue(0)
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 0)
        q.enqueue(9)
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.dequeue(), 1)
        q.dequeue()
        self.assertEqual(q.size(), 0)
        q.enqueue(5)
        self.assertEqual(q.dequeue(), 5)


    def test_queue10(self):
        q = Queue(5)
        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 0)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)

    def test_queue11(self):
        q = Queue(2)
        q.enqueue(0)
        q.enqueue(1)
        with self.assertRaises(IndexError):
            q.enqueue(2)
        q.dequeue()
        q.enqueue(0)
        with self.assertRaises(IndexError):
            q.enqueue(2)
    def test_queue12(self):
        q = Queue(4)
        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.enqueue(0)
        q.enqueue(0)
        q.enqueue(0)
        q.enqueue(0)
        q.dequeue()
        q.enqueue(0)
        with self.assertRaises(IndexError):
            q.enqueue(4)

    def test_queue13(self):
        q = Queue(0)
        with self.assertRaises(IndexError):
            q.enqueue(1)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_queue14(self):
        q = Queue(4)
        q.enqueue(0)
        q.enqueue(1)
        q.dequeue()
        q.dequeue()
        with self.assertRaises(IndexError):
            q.dequeue()
        q.enqueue(0)
        q.dequeue()
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_queue15(self):
        q = Queue(4)
        q.enqueue(2)
        q.enqueue(2)
        q.enqueue(2)
        q.enqueue(2)
        q.dequeue()
        q.enqueue(2)
        with self.assertRaises(IndexError):
            q.enqueue(2)

    def test_queue16(self):
        q = Queue(4)
        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.dequeue()
        q.dequeue()
        self.assertEqual(q.size(), 2)
        q.enqueue(69)
        self.assertEqual(q.dequeue(), 2)

    def test_queue17(self):
        q = Queue(4)
        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.size(), 3)
        q.dequeue()
        q.dequeue()
        self.assertEqual(q.size(), 1)
        q.enqueue(9)
        self.assertEqual(q.size(), 2)
        q.enqueue(10)
        self.assertEqual(q.size(), 3)
        q.enqueue(11)
        self.assertTrue(q.is_full())
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 9)
        self.assertEqual(q.dequeue(), 10)
        self.assertEqual(q.dequeue(), 11)

    def test_queue18(self):
        q = Queue(5)
        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_queue19(self):
        q = Queue(3)
        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 0)
        q.enqueue(23)
        self.assertEqual(q.dequeue(), 1)
        q.enqueue(94)
        self.assertEqual(q.dequeue(), 2)
        q.enqueue(14)
        self.assertEqual(q.dequeue(), 23)
        q.enqueue(145)
        self.assertTrue(q.is_full())


if __name__ == '__main__': 
    unittest.main()
