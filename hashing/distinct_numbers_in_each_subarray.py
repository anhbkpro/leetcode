from typing import List


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq = {}
        left = 0
        for i, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1
            if i >= k - 1:
                ans.append(len(freq))
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return ans
