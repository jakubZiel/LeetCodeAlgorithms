from cmath import inf
import math
from typing import List

def dungeon_game(dungeon : List[List[int]]) -> int:

    dp = [[math.inf for _ in range(len(dungeon[0]) + 1)] for _ in range(len(dungeon) + 1)]
    
    for y in range(len(dungeon) - 1, -1, -1):
        for x in range(len(dungeon[0]) - 1, -1, -1):
            least_health_path = min(dp[y + 1][x], dp[y][x + 1])

            if dungeon[y][x] < 0:
                dp[y][x] = -dungeon[y][x]

                if least_health_path != math.inf:
                    dp[y][x] += least_health_path

            else:
                dp[y][x] = 0
                
                if least_health_path != math.inf and dungeon[y][x] < least_health_path:
                    dp[y][x] = least_health_path - dungeon[y][x]

    return dp[0][0] + 1

board = [
    [-2,-3,3],
    [-5,-10,1],
    [10,30,-5]
    ]

print(dungeon_game(board))