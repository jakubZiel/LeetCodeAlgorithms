from typing import List
import math


def increasing_triplet(nums: List[int]) -> bool:

    max_val = [-math.inf] * len(nums) 

    max_val[len(nums) - 1] = nums[len(nums) - 1]

    for i in range(len(nums) - 2, -1, -1):
        max_val[i] = max(max_val[i + 1], nums[i])
        

    for i in range(0, len(nums) - 1):
        for j in range(i, len(nums) - 1):
            if nums[i] < nums[j] and nums[j] < max_val[j + 1]:
                return True

    return False


#nums = [5,4,3,2,1]
nums = [2,1,5,0,4,6]

print(increasing_triplet(nums))