from typing import List


def separateDigits(nums: List[int]) -> List[int]:
    return [int(d) for n in nums for d in str(n)]


class Solution:
    pass
