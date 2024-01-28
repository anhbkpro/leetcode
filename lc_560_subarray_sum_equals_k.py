from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def subarraySum(nums: List[int], k: int) -> int:
        count = defaultdict()
        count[0] = 1
        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum += num
            ans += count.get(prefix_sum - k, 0)
            if prefix_sum not in count:
                count[prefix_sum] = 0

            count[prefix_sum] += 1

        return ans
