import unittest
from red_black_priority_queue import RedBlackPriorityQueue

class TestRedBlackPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = RedBlackPriorityQueue()

    def test_insert_And_peek(self):

        self.pq.insert("Low", 10)
        self.pq.insert("High", 100)
        self.pq.insert("Mid", 50)

        value, priority = self.pq.peek()
        self.assertEqual(value, "High")
        self.assertEqual(priority, 100)

    def test_pop(self):
        
        self.pq.insert("A", 10)
        self.pq.insert("B", 20)
        self.pq.insert("C", 30)

        self.assertEqual(self.pq.pop(), ("C", 30))
        self.assertEqual(self.pq.pop(), ("B", 20))
        self.assertEqual(self.pq.pop(), ("A", 10))

    def test_empty_queue(self):

        self.assertIsNone(self.pq.peek())
        self.assertIsNone(self.pq.pop())

    def test_same_priority(self):

        self.pq.insert("First", 50)
        self.pq.insert("Second", 50)

        self.assertEqual(self.pq.pop(), ("Second", 50))
        self.assertEqual(self.pq.pop(), ("First", 50))

if __name__ == "__main__":
    unittest.main()