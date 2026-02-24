import unittest
from lab2 import max_hamster

def parse(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    raw_hamsters = list(map(int, lines[0].split()))
    
    hamsters = [
        [raw_hamsters[i], raw_hamsters[i+1]] 
        for i in range(0, len(raw_hamsters), 2)
    ]
    
    C = len(hamsters)
    S = int(lines[1].strip())
    
    return S, C, hamsters

class Test(unittest.TestCase):
    
    def test_from_txt_file(self):
        S, C, hamsters = parse('data.txt')
        result, iterations = max_hamster(S, C, hamsters)
        
        print(f"Hamsters {result}")
        print(f"Iterations: {iterations}")
        
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)