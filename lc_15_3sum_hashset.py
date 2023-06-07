from typing import List


def twoSumSet(nums: List[int], i: int, answer: List[List[int]]) -> None:
    seen = set()
    j = i + 1
    while j < len(nums):
        complement = -nums[i] - nums[j]
        if complement in seen:
            answer.append([nums[i], nums[j], complement])
            while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                j += 1
        seen.add(nums[j])
        j += 1


def threeSumSet(nums: List[int]) -> List[List[int]]:
    answer = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            twoSumSet(nums, i, answer)
    return answer


class Solution:
    pass

