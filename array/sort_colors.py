from typing import List
from collections import Counter


def sort_colors(nums : List[int]) ->  None:
    counts = Counter(nums)
    for i in range(0, counts[0]):
        nums[i] = 0
    end1 = counts[0] + counts[1]
    for i in range(counts[0], end1):
        nums[i] = 1
    for i in range(end1, end1 + counts[2]):
        nums[i] = 2
        

def sort_colors2(nums : List[int]) -> None:
    left = 0
    right = len(nums) - 1

    def swap(i : int, j : int) -> None:
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    i = 0
    while i < right:
        if nums[i] == 0:
            swap(i, left)
            left += 1
        elif nums[i] == 2:
            swap(i, right)
            right -= 1
            i -= 1
        i += 1

nums = [2,0,2,1,1,0, 1, 1, 0]

sort_colors2(nums)
print(nums)
