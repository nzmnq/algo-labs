import unittest
import os
from bucket_mode import process_file

class TestFloodFill(unittest.TestCase):
    def test_file_processing(self):
        input_data = (
            "10,10\n"
            "3,9\n"
            "C\n"
            "['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],\n"
            "['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],\n"
            "['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],\n"
            "['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],\n"
            "['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],\n"
            "['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],\n"
            "['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],\n"
            "['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],\n"
            "['W', 'B', 'B', 'X', 'B', 'B', 'B', 'X', 'X', 'X'],\n"
            "['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']\n"
        )

        with open('input.txt', 'w', encoding='utf-8') as f:
            f.write(input_data)
            
        process_file('input.txt', 'output.txt')

        with open('output.txt', 'r', encoding='utf-8') as f:
            content = f.read().strip()

        expected =(
            "['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],\n"
            "['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'C', 'C', 'C'],\n"
            "['G', 'G', 'G', 'G', 'G', 'G', 'G', 'C', 'C', 'C'],\n"
            "['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'C'],\n"
            "['W', 'R', 'R', 'R', 'R', 'R', 'G', 'C', 'C', 'C'],\n"
            "['W', 'W', 'W', 'R', 'R', 'G', 'G', 'C', 'C', 'C'],\n"
            "['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'C'],\n"
            "['W', 'B', 'B', 'B', 'B', 'R', 'R', 'C', 'C', 'C'],\n"
            "['W', 'B', 'B', 'C', 'B', 'B', 'B', 'C', 'C', 'C'],\n"
            "['W', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C']"
        )

        self.assertEqual(content, expected)
        
        if os.path.exists('input.txt'):
            os.remove('output.txt')

if __name__ == '__main__':
    unittest.main()