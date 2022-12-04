from typing import List
import math
from collections import deque



def matrix_01(matrix: List[List[int]]) -> List[List[int]]:
    COLS = len(matrix[0])
    ROWS = len(matrix)

    queue = deque() 

    for row in range(ROWS):
        for column in range(COLS):
            if matrix[row][column] == 0:
                queue.append((row, column, 0))

    output = [[math.inf for _ in range(COLS)] for _ in range(ROWS)]

    while queue:
        row, col, distance = queue.popleft()

        if output[row][col] != math.inf:
            continue
            
        output[row][col] = min(output[row][col], distance)
        
        if col + 1 < len(output[0]) and output[row][col + 1] == math.inf:
            queue.append((row, col + 1, distance + 1))

        if col - 1 > -1 and output[row][col - 1] == math.inf:
            queue.append((row, col - 1, distance + 1))
        
        if row + 1 < len(output) and output[row + 1][col] == math.inf:
            queue.append((row + 1, col, distance + 1))
        
        if row - 1 > - 1 and output[row - 1][col] == math.inf:
            queue.append((row - 1, col, distance + 1))

    return output

matrix =  [[0,0,0],[0,1,0],[1,1,1]]

dist_matrix = matrix_01(matrix)

for row in dist_matrix:
    print(row)