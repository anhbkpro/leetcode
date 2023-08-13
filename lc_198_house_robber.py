from typing import List


class Solution:

    @staticmethod
    def rob(nums: List[int]) -> int:

        # Special handling for empty case.
        if not nums:
            return 0

        n = len(nums)

        rob_next_plus_one = 0
        rob_next = nums[n - 1]

        # DP table calculations.
        for i in range(n - 2, -1, -1):
            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])

            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current

        return rob_next
