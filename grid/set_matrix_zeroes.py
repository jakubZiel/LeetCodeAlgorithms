from typing import List
def set_matrix_zeroes(matrix : List[List[int]]) -> None:
    rows = set()
    colums = set()
    ROWS = len(matrix)
    COLUMNS = len(matrix[0])


    for y in range(ROWS):
        for x in range(COLUMNS):
            if matrix[y][x] == 0:
                rows.add(y)
                colums.add(x)

    for row in rows:
        for x in range(COLUMNS):
            matrix[row][x] = 0

    for column in colums:
        for y in range(ROWS):
            matrix[y][column] = 0

matrix = [
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 1],
]

set_matrix_zeroes(matrix)

print(matrix)