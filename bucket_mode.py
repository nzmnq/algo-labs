import ast
'''flood fill algorithm'''
def flood_fill(matrix, r, c, replacement_color):
    rows = len(matrix)
    cols = len(matrix[0])
    target_color = matrix[r][c]

    if target_color == replacement_color:
        return matrix

    queue = [(r, c)]
    matrix[r][c] = replacement_color

    while queue:
        curr_r, curr_c = queue.pop(0)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == target_color:
                matrix[nr][nc] = replacement_color
                queue.append((nr, nc))

    return matrix
'''processing file'''
def process_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    dimensions = lines[0].strip().split(',')
    rows = int(dimensions[0])
    cols = int(dimensions[1])

    start_coords = lines[1].strip().split(',')
    start_r = int(start_coords[0])
    start_c = int(start_coords[1])

    replacement_color = lines[2].strip().strip("'").strip('"')

    matrix = []
    for line in lines[3:]:
        cleaned_line = line.strip()
        if cleaned_line.endswith(','):
            cleaned_line = cleaned_line[:-1]
        if cleaned_line:
            row_data = ast.literal_eval(cleaned_line)
            matrix.append(row_data)

    filled_matrix = flood_fill(matrix, start_r, start_c, replacement_color)

    with open(output_filename, 'w', encoding='utf-8') as f:
        for i, row in enumerate(filled_matrix):
            if i < len(filled_matrix) - 1:
                f.write(str(row) + ',\n')
            else:
                f.write(str(row) + '\n')

if __name__ == '__main__':
    process_file('input.txt', 'output.txt')