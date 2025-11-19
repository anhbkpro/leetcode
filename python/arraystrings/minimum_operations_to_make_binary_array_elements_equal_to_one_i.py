from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                cnt += 1
                if i + 2 >= n:
                    return -1

                if i + 1 == n - 1 and nums[i + 1] != nums[i]:
                    return -1
                if i + 2 == n - 1 and nums[i + 2] != nums[i]:
                    return -1
                nums[i] = 1

                if i + 1 < n:
                    nums[i + 1] = nums[i + 1] ^ 1
                if i + 2 < n:
                    nums[i + 2] = nums[i + 2] ^ 1

        return cnt
