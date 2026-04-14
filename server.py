class MinHeap:
    '''Priorty queue'''
    def __init__(self):
        self.heap = []
        
    def push(self, item):
        '''Adding new elements'''
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        '''Deleting elements'''
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx][0] < self.heap[parent][0]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        '''Diving'''
        n = len(self.heap)
        while True:
            smallest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2

            if left < n and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < n and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest != idx:
                self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
                idx = smallest
            else:
                break
    
    def is_empty(self):
        return len(self.heap) == 0


def solve_gamsrv(n, clients, edges):
    '''Main solution for our task'''
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges: # Because the main graph is undirected we add elements to both sides
        graph[u].append((v, w))
        graph[v].append((u, w))

    clients_set = set(clients)
    potential_servers = [i for i in range(1, n + 1) if i not in clients_set]

    min_max_latency = float('inf')

    def dijkstra(start_node):
        '''Dijkstra Algorithm'''
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[start_node] = 0
        pq = MinHeap()
        pq.push((0, start_node))

        while not pq.is_empty():
            current_dist, current_node = pq.pop()

            if current_dist > distances[current_node]:
                continue

            for neighbor, weight in graph[current_node]:
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    pq.push((distance, neighbor))

        return distances

    for server in potential_servers:
        distances = dijkstra(server)
        
        max_latency_for_server = 0
        for client in clients_set:
            if distances[client] > max_latency_for_server:
                max_latency_for_server = distances[client]

        if max_latency_for_server < min_max_latency:
            min_max_latency = max_latency_for_server

    return min_max_latency