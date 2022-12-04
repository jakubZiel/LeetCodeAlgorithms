from typing import List
from collections import deque


def aware_of_secret(delay: int, forget: int, n: int) -> int:

    aware = deque()
    aware.append((delay, forget, 1))

    for day in range(1, n + 1):
        next_aware = deque()

        while aware:
            p_delay, p_forget, p_day = aware.pop()

            if p_forget == 0:
                continue
            
            if p_delay <= 0:
                next_aware.append((delay - 1, forget - 1, p_day + 1))

            next_aware.append((p_delay - 1, p_forget - 1, day + 1))
        
        aware = next_aware

    return len(next_aware)


print(aware_of_secret(1,3, 4))