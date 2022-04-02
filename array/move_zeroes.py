from typing import List

def move_zeroes(array : List[int]) -> List[int] :
    sorted_ptr : int = 0

    ptr : int = 0

    while ptr < len(array):
        if array[ptr] != 0:
            array[sorted_ptr] = array[ptr]
            sorted_ptr += 1
        ptr += 1
    while sorted_ptr < len(array):
        array[sorted_ptr] = 0
        sorted_ptr += 1

    return array

array = [0, 1, 2, 3, 4, 0, 5]

print(move_zeroes(array))