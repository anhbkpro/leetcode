from typing import List


#  Time Complexity: O(n)
#  Space Complexity: O(1)
def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    for i in range(len(nums)):
        if target - nums[i] in d:
            return [d[target - nums[i]], i]
        d[nums[i]] = i
    return None


class Solution:
    pass
