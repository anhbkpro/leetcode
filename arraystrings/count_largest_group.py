import collections


class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_map = collections.Counter()
        for i in range(1, n + 1):
            local_sum = 0
            while i > 0:
                local_sum += i % 10
                i //= 10
            sum_map[local_sum] += 1
        max_value = max(sum_map.values())
        count = sum(1 for v in sum_map.values() if v == max_value)
        return count
