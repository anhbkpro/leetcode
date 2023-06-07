from typing import List


def twoSum(nums: List[int], i: int, answer: List[List[int]]) -> None:
    lo, hi = i + 1, len(nums) - 1
    while lo < hi:
        sum = nums[i] + nums[lo] + nums[hi]
        if sum < 0:
            lo += 1
        elif sum > 0:
            hi -= 1
        else:
            answer.append([nums[i], nums[lo], nums[hi]])
            lo += 1
            hi -= 1
            while lo < hi and nums[lo] == nums[lo - 1]:
                lo += 1


def threeSum(nums: List[int]) -> List[List[int]]:
    answer = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            twoSum(nums, i, answer)
    return answer


class Solution:
    pass

