from typing import List

class range_query_2d:
    def __init__(self, matrix : List[List[int]]) -> None:
        self.matrix = matrix
        self.cache = [[0 for x in range(0, len(matrix[0]) + 1)] for y in range(0, len(matrix) + 1)]
        self.init_cache(self.cache)

    def init_cache(self, cache):
        for y in range(1, len(matrix) + 1):
            for x in range(1, len(matrix[0]) + 1):
                cache[y][x] = matrix[y - 1][x - 1] + cache[y - 1][x] + cache[y][x - 1] - cache[y - 1][x - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        row1 += 1; col1 += 1; row2 +=1; col2 += 1

        return self.cache[row2][col2] - self.cache[row2][col1 - 1] - self.cache[row1 - 1][col2] + self.cache[row1 - 1][col1 - 1]


matrix = [
        [3, 0, 1, 4, 2], 
        [5, 6, 3, 2, 1], 
        [1, 2, 0, 1, 5], 
        [4, 1, 0, 1, 7], 
        [1, 0, 3, 0, 5]
    ]

range_query_solver = range_query_2d(matrix)
print(range_query_solver.sumRegion(1, 1, 2, 2))