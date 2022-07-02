from typing import List

def first_missing_positive(nums : List[int]) -> int:
    for i in range(0, len(nums)):
        if nums[i] <= 0:
            nums[i] = None

    for i in range(0, len(nums)):
        if nums[i] is None or nums[i] == "FOUND":
            continue
        pos_integer_index = abs(nums[i]) - 1
        
        if pos_integer_index > len(nums) - 1:
            continue
        if nums[pos_integer_index] is None or nums[pos_integer_index] == "FOUND":
            nums[pos_integer_index] = "FOUND"
        else:
            if nums[pos_integer_index] > 0:
                nums[pos_integer_index] *= -1
    
    for number in range(1, len(nums) + 1):
        if nums[number - 1] == "FOUND":
            continue
        if nums[number - 1] is None or nums[number - 1] > 0:
            return number
    return len(nums) + 1
    
nums = [7,8,9,11,12]
nums2 = [3,4,-1,1]
nums3 = [2, 0 ,1]
nums4 = [1]
print(first_missing_positive(nums3))
