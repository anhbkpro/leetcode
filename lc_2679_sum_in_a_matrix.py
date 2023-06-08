from typing import List


def matrix_sum(nums: List[List[int]]) -> int:
    new_nums = []
    for row in nums:
        new_nums.append(sorted(row, reverse=True))
    trans = zip(*new_nums)
    s = 0
    for i in trans:
        print(i)
        print(f"max of {i} = {max(i)}")
        s += max(i)
    return s


class Solution:
    pass
