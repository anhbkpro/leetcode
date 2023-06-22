import collections
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    left, right, ans = 0, 0, 0
    counter = collections.Counter()
    n = len(nums)

    while right < n:
        counter[nums[right]] += 1
        right += 1
        if counter[0] > 1:
            counter[nums[left]] -= 1
            left += 1

        ans = max(ans, counter[0] + counter[1])

    return ans


class Solution:
    pass
