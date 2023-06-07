from typing import List


#  Time Complexity: O(n)
#  Space Complexity: O(1)
def twoSum(nums: List[int], target: int) -> List[int]:
    """Approach 3: One-pass Hash Table"""
    hashmap = {}
    for i in range(len(nums)):
        if target - nums[i] in hashmap:
            return [hashmap[target - nums[i]], i]
        hashmap[nums[i]] = i
    return None


def twoSum2Loops(nums: List[int], target: int) -> List[int]:
    """Approach 2: Two-pass Hash Table"""
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]


class Solution:
    pass
