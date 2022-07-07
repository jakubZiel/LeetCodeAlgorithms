from typing import List
from math import inf

def pick_fruits(fruits: List[int]) -> int:
    beg = 0
    end = 0
    total = 0
    window_values = {}
    max_seq = -inf

    while end < len(fruits)    :
        fruit = fruits[end]

        if fruit in window_values:
            window_values[fruit] += 1
            total += 1
            max_seq = max(max_seq, total)
            end += 1
        else:
            if len(window_values) == 2:
                while beg <= end and len(window_values) >= 2:
                    fruit = fruits[beg]
                    window_values[fruit] -= 1
                    total -= 1

                    if window_values[fruit] == 0:
                        del window_values[fruit]
                    beg += 1
            else:
                window_values[fruit] = 1
                total += 1
                end += 1
                max_seq = max(max_seq, total)
    return max_seq, fruits[beg:end + 1]


fruits = [1,2,3,2,2]

print(pick_fruits(fruits))