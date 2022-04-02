import math
from typing import List, Dict, Tuple

def min_path_sum(grid : List[List[int]]) -> int:

    ROWS = len(grid)
    COLS = len(grid[0])
    cache = [[math.inf for x in range(0, COLS + 1)] for y in range(0, ROWS + 1)]

    cache[ROWS][COLS - 1] = 0

    for y in range(ROWS - 1, -1, -1):
        for x in range(COLS - 1, -1, -1):
            cache[y][x] = grid[y][x] + min(cache[y + 1][x], cache[y][x + 1])

    return cache[0][0]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(min_path_sum(grid))