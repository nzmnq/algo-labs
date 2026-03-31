import unittest
import os
from bucket_mode import flood_fill, process_file

class TestFloodFill(unittest.TestCase):
    def test_flood_fill(self):
        matrix = [
            ['Y', 'G', 'X'],
            ['Y', 'X', 'X'],
            ['B', 'B', 'X']
        ]
        expected = [
            ['Y', 'G', 'C'],
            ['Y', 'C', 'C'],
            ['B', 'B', 'C']
        ]
        result = flood_fill(matrix, 0, 2, 'C')
        self.assertEqual(result, expected)

    def test_file_processing(self):
        with open('input.txt', 'w', encoding='utf-8') as f:
            f.write("3,3\n0,2\n'C'\n['Y', 'G', 'X'],\n['Y', 'X', 'X'],\n['B', 'B', 'X']\n")
        
        process_file('input.txt', 'output.txt')
        
        with open('output.txt', 'r', encoding='utf-8') as f:
            content = f.read().strip()
            
        expected = "['Y', 'G', 'C'],\n['Y', 'C', 'C'],\n['B', 'B', 'C']"
        self.assertEqual(content, expected)
        
        os.remove('output.txt')

if __name__ == '__main__':
    unittest.main()