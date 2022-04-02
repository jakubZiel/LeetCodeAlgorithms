from typing import List
def capture_regions(grid : List[List[int]]) -> List[List[int]]:
    ROWS = len(grid)
    COLS = len(grid[0])

    visited = [[False for x in range(0, COLS)] for y in range(0, ROWS)]
    uncaptured = set()

    def dfs(y_pos : int, x_pos : int) -> None:
        stack = [(y_pos, x_pos)]

        while stack:    
            y, x = stack.pop()
            visited[y][x] = True
            
            if grid[y][x] == 'O':
                uncaptured.add((y, x))

                if y + 1 < ROWS and not visited[y + 1][x]:
                    stack.append((y + 1, x))
                if y - 1 > -1 and not visited[y - 1][x]:
                    stack.append((y - 1, x))
                if x + 1 < COLS and not visited[y][x + 1]:
                    stack.append((y, x + 1))
                if x - 1 > -1 and not visited[y][x - 1]:
                    stack.append((y, x - 1))
                    
    for x in range(0, COLS):
        dfs(0, x)
        dfs(ROWS - 1, x)

    for y in range(0, ROWS):
        dfs(y, 0)
        dfs(y, COLS - 1)

    for y in range(0, ROWS):
        for x in range(0, COLS):
            if not uncaptured.__contains__((y, x)) and grid[y][x] == 'O':
                grid[y][x] = 'X'

    return grid


board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]

board2 = [["X"]]


captured = capture_regions(board)

for line in captured:
    print(line)