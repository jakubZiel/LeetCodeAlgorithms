from typing import List
from bisect import bisect_left


#An integer a is closer to x than an integer b if:
#|a - x| < |b - x|, or
#|a - x| == |b - x| and a < b

def find_k_closest(nums : List[int], k : int, target : int) -> List[int]:
    def closest_dist(index1 : int, index2 : int) -> int:
        cand1 = nums[index1]
        cand2 = nums[index2]

        if abs(cand1 - target) == abs(cand2 - target):
            if cand1 < cand2:
                return index1
            else:
                return index2
        elif abs(cand1 - target) < (abs(cand2 - target)):
            return index1
        else:
            return index2

    closest = bisect_left(nums, target)

    if closest == len(nums):
        return nums[len(nums) - k:len(nums)]
    elif nums[closest] != target and closest != 0:
        closest = closest_dist(closest, closest - 1)

    left = right = closest
    while right - left + 1 < k:
        if left == 0:
            return nums[0:k]
        if right == len(nums) - 1:
            return nums[len(nums) - k:len(nums)]

        index = closest_dist(left - 1, right + 1)

        if index == left - 1:
            left -= 1
        else:
            right += 1
    return nums[left:right + 1]



nums = [0,0,1,2,3,3,4,7,7,8]
k = 3
target = 5

print(find_k_closest(nums, k, target))


print(bisect_left([3, 5, 8, 10],15))