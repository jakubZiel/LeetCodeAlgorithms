import math
from typing import List, Set

def find_max_performance(speed_list: List[int], efectivness_list: List[int], k: int, n: int) -> int:
    engineers = list(zip(efectivness_list, speed_list))
    engineers.sort(key=lambda engineer: engineer[0], reverse=True)
    engineers = [(math.inf, 0)] + engineers

    return 0
    
speed = [2,10,3,1,5,8]
effectivness = [5,4,3,9,7,2]
k = 2


find_max_performance(speed, effectivness, k, len(speed))