from typing import List


class Solution:
    def _is_valid(self, nums: List[int], k: int, mid_reward: int) -> bool:
        total_houses = len(nums)
        possible_thefts = 0
        index = 0
        while index < total_houses:
            if nums[index] <= mid_reward:
                possible_thefts += 1
                index += 2
            else:
                index += 1
        return possible_thefts >= k

    def minCapability(self, nums: List[int], k: int) -> int:
        min_reward, max_reward = 0, max(nums)

        while min_reward < max_reward:
            mid_reward = (min_reward + max_reward) // 2
            if self._is_valid(nums, k, mid_reward):
                max_reward = mid_reward
            else:
                min_reward = mid_reward + 1

        return min_reward
