import unittest
from lab3 import BinaryTree
from lab3 import find_successor
class TestFindSuccessor(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(10)
        
        self.node_5 = BinaryTree(5, parent=self.root)
        self.node_15 = BinaryTree(15, parent=self.root)
        self.root.left = self.node_5
        self.root.right = self.node_15
        
        self.node_3 = BinaryTree(3, parent=self.node_5)
        self.node_7 = BinaryTree(7, parent=self.node_5)
        self.node_5.left = self.node_3
        self.node_5.right = self.node_7
        
        self.node_12 = BinaryTree(12, parent=self.node_15)
        self.node_20 = BinaryTree(20, parent=self.node_15)
        self.node_15.left = self.node_12
        self.node_15.right = self.node_20

    def test_successor_for_7(self):
        successor = find_successor(self.root, self.node_7)
        self.assertIsNotNone(successor)
        self.assertEqual(successor.value, 10)
if __name__ == "__main__":
     unittest.main()