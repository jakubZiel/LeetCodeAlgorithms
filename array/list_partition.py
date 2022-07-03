from mimetypes import init
from typing import List
from random import shuffle


def list_partition(nums: List[int], target: int) -> List[int]:
    def swap(index1, index2):
        tmp = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = tmp
    
    less_index = 0
    more_index = len(nums) - 1

    curr = 0

    while curr <= more_index:
        curr_val = nums[curr]

        if curr_val > target:
            if curr == more_index:
                curr -= 1
            else:
                swap(curr, more_index)
            
            more_index -= 1

        elif curr_val < target:
            if curr == less_index:
                curr += 1
            else:
                swap(curr, less_index)

            less_index += 1
        else:
            curr += 1

    return nums, less_index, more_index

target = 5
nums = [0, 1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 8, 12, 14, 14, 15, 15, 18, 22]
init_nums = nums.copy()

shuffle(nums)

nums, less_index, more_index = list_partition(nums, target)

def validate_less(nums: List[int], target: int) -> bool:
    for val in nums:
        if val > target:
            return False
    return True

def validate_more(nums: List[int], target: int) -> bool:
    for val in nums:
        if val < target:
            return False
    return True

def validate_equal(nums: List[int], target: int) -> bool:
    for val in nums:
        if val != target:
            return False
    return True

print("\nnums was : " + str(init_nums))
print("\nnums is  : " + str(nums))
print("\ntarget is : " + str(target) + "\n")

print(nums[0:less_index])
print(validate_less(nums[0:less_index], target), end='\n\n')

print(nums[less_index:more_index + 1])
print(validate_equal(nums[less_index:more_index + 1], target), end='\n\n')

print(nums[more_index + 1:len(nums)])
print(validate_more(nums[more_index + 1:len(nums)], target), end='\n\n')