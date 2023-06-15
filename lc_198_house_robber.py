from typing import List


def rob(nums: List[int]) -> int:

    # Special handling for empty case.
    if not nums:
        return 0

    max_robbed_amount = [None for _ in range(len(nums) + 1)]
    n = len(nums)
    # Base case initialization.
    max_robbed_amount[n], max_robbed_amount[n - 1] = 0, nums[n - 1]

    # DP table calculations.
    for i in range(n - 2, -1, -1):
        print(i)
        # Same as recursive solution.
        # option 1: do nothing
        # option 2: rob house i and i + 2
        max_robbed_amount[i] = max(max_robbed_amount[i + 1], max_robbed_amount[i + 2] + nums[i])
        print(f"maxRobbedAmount[{i}]={max_robbed_amount[i]}")

    return max_robbed_amount[0]


class Solution:
    pass
