from typing import List

triangle = [
    [2],
    [3, 4],
    [6, 5, 4],
    [4, 1, 8, 3]
]

def min_path(triangle : List[List[int]]) -> int:
    
    cache = {}

    def recurse(level : int, pos :  int) -> int:
        if level == len(triangle) - 1:
            return triangle[len(triangle) - 1][pos]

        below = recurse(level + 1, pos)
        diagonal = recurse(level + 1, pos + 1)

        cache[(level, pos)] = min(below, diagonal) + triangle[level][pos]

        return cache[((level, pos))]

    return recurse(0, 0)

print(min_path(triangle))