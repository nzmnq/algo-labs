class TribeGraph:
    def __init__(self):
        self.data = {}

    def add_connection(self, person1, person2):
        if person1 not in self.data:
            self.data[person1] = []
        self.data[person1].append(person2)
        
        if person2 not in self.data:
            self.data[person2] = []
        self.data[person2].append(person1)

    def get_neighbors(self, person):
        return self.data.get(person, [])

    def get_all_people(self):
        return self.data.keys()

def count_valid_pairs(n: int, pairs: list[tuple[int, int]]) -> int:
    if n == 0 or not pairs:
        return 0

    graph = TribeGraph()
    for u, v in pairs:
        graph.add_connection(u, v)

    visited = set()
    tribes_stats = []
    
    total_boys = 0
    total_girls = 0

    for person in graph.get_all_people():
        if person not in visited:
            tribe_boys = 0
            tribe_girls = 0
            
            queue = [person]
            visited.add(person)
            
            while queue:
                curr = queue.pop(0)
                
                if curr % 2 != 0:
                    tribe_boys += 1
                else:
                    tribe_girls += 1
                    
                for neighbor in graph.get_neighbors(curr):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        
            tribes_stats.append((tribe_boys, tribe_girls))
            total_boys += tribe_boys
            total_girls += tribe_girls

    total_possible_pairs = total_boys * total_girls
    
    invalid_pairs = 0
    for boys_in_tribe, girls_in_tribe in tribes_stats:
        invalid_pairs += boys_in_tribe * girls_in_tribe

    return total_possible_pairs - invalid_pairs