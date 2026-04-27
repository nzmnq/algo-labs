import csv

def get_minimum_length(filename):
    matrix = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                numeric_row = [float(val) for val in row if val.strip()]
                if numeric_row:
                    matrix.append(numeric_row)

    except FileNotFoundError:
        return "Error, islands.csv not found"

    n = len(matrix)
    if n <= 1:
        return 0.0

    connected_islands = [False] * n
    connected_islands[0] = True
    total_cable_length = 0.0
    connections_made = 0

    while connections_made < n - 1:
        min_distance = float('inf')
        island_from = -1
        island_to = -1

        for i in range(n):
            if connected_islands[i]:
                for j in range(n):
                    if not connected_islands[j] and matrix[i][j] > 0:
                        if matrix[i][j] < min_distance:
                            min_distance = matrix[i][j]
                            island_from = i
                            island_to = j

        if min_distance != float('inf'):
            connected_islands[island_to] = True
            total_cable_length += min_distance
            connections_made += 1
        else:
            return "Error, graph is not connected"

    return total_cable_length

if __name__ == "__main__":
    result = get_minimum_length('islands.csv')
    print(f"Minimal length of underwater cables: {result}")