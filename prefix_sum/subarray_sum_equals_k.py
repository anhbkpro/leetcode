from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def subarray_sum(nums: List[int], k: int) -> int:
        sum_occurrences_map = defaultdict(int)
        sum_occurrences_map[0] = 1
        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum += num
            ans += sum_occurrences_map.get(prefix_sum - k, 0)
            if prefix_sum not in sum_occurrences_map:
                sum_occurrences_map[prefix_sum] = 0

            sum_occurrences_map[prefix_sum] += 1

        return ans
