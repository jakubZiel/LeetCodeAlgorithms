from typing import List

def card_points(cards : List[int], k : int) -> int:
    l_ptr = k - 1
    r_ptr = len(cards) - 1

    l_sum = sum(cards[:k])
    r_sum = 0
     
    max_sum = l_sum

    while l_ptr > -1 :
        
        r_sum += cards[r_ptr]
        l_sum -= cards[l_ptr]

        r_ptr -= 1
        l_ptr -= 1

        max_sum = max(max_sum, l_sum + r_sum)
    
    return max_sum

cards = [1, 2, 3, 4, 5, 6, 1]

print(card_points(cards , 3))