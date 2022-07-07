from typing import List
from math import inf

def pick_fruits(fruits: List[int]) -> int:
    fruits_seq = []
    curr = fruits[0]
    seq = 0
    for i in range(len(fruits)):
        if fruits[i] == curr:
            seq += 1
        else:
            fruits_seq.append((curr, seq))
            curr = fruits[i]
            seq = 1

        if i == len(fruits) - 1:
            fruits_seq.append((curr, seq))
    
    beg = 0
    end = 0
    total = 0
    window_values = {}
    max_seq = -inf

    while end < len(fruits_seq)    :
        fruit, count = fruits_seq[end]

        if fruit in window_values:
            window_values[fruit] += count
            total += count
            max_seq = max(max_seq, total)
            end += 1
        else:
            if len(window_values) == 2:
                while beg <= end and len(window_values) >= 2:
                    fruit, count = fruits_seq[beg]
                    window_values[fruit] -= count
                    total -= count

                    if window_values[fruit] == 0:
                        del window_values[fruit]
                    beg += 1
            else:
                window_values[fruit] = count
                total += count
                end += 1
                max_seq = max(max_seq, total)
    return max_seq, fruits_seq[beg:end + 1]


fruits = [1,2,3,2,2]

print(pick_fruits(fruits))