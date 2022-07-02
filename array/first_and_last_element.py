from typing import List, Tuple

def find_first_and_last(nums: List[int], target: int) -> Tuple[int, int]:
    
    def middle(left_index: int, right_index: int) -> int:
        return (left_index + right_index) // 2   
 
    def find_target() -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = middle(left, right)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
    
    def find_first(target_index: int) -> int:
        left = 0
        right = target_index

        while left <= right:
            mid = middle(left, right)

            if not nums[mid] == target:
                if nums[mid + 1] == target:
                    return mid + 1
                else:
                    left = mid + 1
            else:
                if mid == 0:
                    return mid

                if not nums[mid - 1] == target:
                    return mid
                else:
                    right = mid - 1
        return -1
    
    def find_last(target_index: int) -> int:    
        left = target_index
        right = len(nums) - 1

        while left <= right:
            mid = middle(left, right)

            if not nums[mid] == target:
                if nums[mid - 1] == target:
                    return mid - 1
                else:
                    right = mid - 1
            else:
                if mid == len(nums) - 1:
                    return mid
                
                if not nums[mid + 1] == target:
                    return mid
                else:
                    left = mid + 1
        return -1

    if not nums:
        return [-1, -1]

    target_index = find_target()

    if not nums[target_index] == target:
        return (-1, -1)

    
    first = find_first(target_index)
    last = find_last(target_index)

    return (first, last)


nums = [5,7,7,8,8,10]

target = 1
first, last = find_first_and_last(nums, target)


print(str(nums[0:first]) + " + " + str(nums[first:last + 1]) + " + " + str(nums[last + 1:len(nums)]))
