from itertools import count
import math
from typing import List, Set

def min_domino_rotations(tops : List[int], bottoms : List[int]) -> int:

    counts = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
    bottom_count = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
    top_count = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}   
    
    length = len(tops)

    for i in range(0, length):
        if bottoms[i] == tops[i]:
            counts[tops[i]] += 1
        else:
            counts[tops[i]] += 1         
            counts[bottoms[i]] += 1
        
        bottom_count[bottoms[i]] += 1
        top_count[tops[i]] += 1

    
    min_rotations = math.inf

    for number in counts.keys():
        if counts[number] == length:
            min_rotations = min(min_rotations, min(length - bottom_count[number], length - top_count[number]))

    return min_rotations if min_rotations != math.inf else -1

tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]


print(min_domino_rotations(tops, bottoms))