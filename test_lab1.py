import unittest
from lab1_1 import zigzag
class Testzigzag(unittest.TestCase):
    def tets_3_3(self):
        matrix = [
            [1, 2, 6],
            [3, 5, 7],
            [4, 8, 9]
        ]
        self.assertEqual(zigzag(3, 3), matrix)
    def test_5_5(self):
        matrix = [
            [ 1,  2,  6,  7, 15],
            [ 3,  5,  8, 14, 16],
            [ 4,  9, 13, 17, 22],
            [10, 12, 18, 21, 23],
            [11, 19, 20, 24, 25]
        ]
        self.assertEqual(zigzag(5, 5), matrix)
    def test_2_4(self):
        matrix = [
            [1, 2, 5, 6],
            [3, 4, 7, 8]
        ]
        self.assertEqual(zigzag(4, 2), matrix)
    def test_1_6(self):
        matrix = [
            [1],
            [2],
            [3],
            [4],
            [5],
            [6]
        ]
        self.assertEqual(zigzag(1, 6), matrix)
    def test_1_1(self):
        matrix = [
            [1]
        ]
        self.assertEqual(zigzag(1, 1), matrix)
if __name__ == '__main__':
    unittest.main()