import math
from typing import List

def least_bricks(wall: List[List[int]]) -> int:
    spots = {}

    for layer in wall:
        spot = 0
        for brick_index in range(len(layer) - 1):
            
            brick = layer[brick_index]
            spot += brick

            if not spot in spots:
                spots[spot] = 0
            spots[spot] += 1

    max_spots = -math.inf

    for spot in spots.keys():
        max_spots = max(max_spots, spots[spot])


    return len(wall) if len(spots) == 0 else len(wall) - max_spots
    
wall = [
    [1,2,2,1],
    [3,1,2],
    [1,3,2],
    [2,4],
    [3,1,2],
    [1,3,1,1]
]


print(least_bricks(wall))