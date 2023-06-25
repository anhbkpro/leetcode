from typing import List


def largestUniqueNumber(nums: List[int]) -> int:
    hash_map = {}
    for num in nums:
        if num in hash_map:
            hash_map[num] = False
        else:
            hash_map[num] = True

    current_max = -1
    for item in hash_map:
        if hash_map[item] and item > current_max:
            current_max = item

    return current_max


class Solution:
    pass
