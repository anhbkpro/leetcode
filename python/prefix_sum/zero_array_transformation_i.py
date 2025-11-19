from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        queries.sort(key=lambda x: x[0])

        diff = [0] * (len(nums) + 1)
        for s, e in queries:
            diff[s] += 1
            diff[e + 1] -= 1

        current_operations = 0
        operation_counts = []
        for d in diff:
            current_operations += d
            operation_counts.append(current_operations)

        for num, op in zip(nums, operation_counts):
            if num > op:
                return False

        return True
