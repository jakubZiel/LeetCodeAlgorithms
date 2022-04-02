from typing import List

def find_pivot(array : List[int]) -> int:
    sum : int = 0
    left : int = 0
    right : int = 0

    for ele in array:
        sum += ele

    left = 0
    right = sum - array[0]
    
    for index in range(0, len(array)):

        if left == right:
            return index

        left += array[index]
        right -= array[index + 1]

    return -1

array = [1, 7, 3, 6, 5, 6]

print(find_pivot(array))
