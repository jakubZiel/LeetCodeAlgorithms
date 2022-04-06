from typing import List

def sub_islands(grid1 : List[List[int]], grid2 : List[List[int]]) -> int:
    ROWS = len(grid1)
    COLS = len(grid1[0])
    
    sub_islands = 0
    visited = set()
                
    def dfs(start_y : int, start_x : int) -> bool:
        is_sub_island = True
        stack = [(start_y, start_x)]

        while stack:
            y, x = stack.pop()
            visited.add((y, x))

            if grid1[y][x] != grid2[y][x]:
                is_sub_island = False 

            if y + 1 < ROWS and grid2[y + 1][x] != 0 and (y + 1, x) not in visited:
                stack.append((y + 1, x))
            if y - 1 > -1 and grid2[y - 1][x] != 0 and (y - 1, x) not in visited:
                stack.append((y - 1, x))
            if x + 1 < COLS and grid2[y][x + 1] != 0 and (y, x + 1) not in visited:
                stack.append((y, x + 1))
            if x - 1 > -1 and grid2[y][x - 1] != 0 and (y, x - 1) not in visited:
                stack.append((y, x - 1)) 

        return is_sub_island

    for y in range(0, ROWS):
        for x in range(0, COLS):
            if grid2[y][x] == 1 and not visited.__contains__((y, x)) and dfs(y, x):
                sub_islands += 1

    return sub_islands


grid1 = [[1,1,1,1,0,0],[1,1,0,1,0,0],[1,0,0,1,1,1],[1,1,1,0,0,1],[1,1,1,1,1,0],[1,0,1,0,1,0],[0,1,1,1,0,1],[1,0,0,0,1,1],[1,0,0,0,1,0],[1,1,1,1,1,0]]
grid2 = [[1,1,1,1,0,1],[0,0,1,0,1,0],[1,1,1,1,1,1],[0,1,1,1,1,1],[1,1,1,0,1,0],[0,1,1,1,1,1],[1,1,0,1,1,1],[1,0,0,1,0,1],[1,1,1,1,1,1],[1,0,0,1,0,0]]

print(sub_islands(grid1, grid2))