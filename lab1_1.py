def zigzag(n, m):
    if m <= 0 or n <= 0:
        return []
    
    matrix = [[0] * n for _ in range(m)]
    row, col = 0, 0
    direct = 1

    for i in range(1, m * n + 1):
        matrix[row][col] = i
        if direct == 1:
            if col == n - 1:
                row += 1
                direct = -1
            elif row == 0:
                col += 1
                direct = -1
            else:
                row -= 1
                col += 1
        else:
            if row == m - 1:
                col += 1
                direct = 1
            elif col == 0:
                row += 1
                direct = 1
            else:
                row += 1
                col -= 1
    return matrix