from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sum_element(num: int) -> int:
            ans = 0
            while num > 0:
                ans += num % 10
                num //= 10

            return ans

        result = []
        for num in nums:
            result.append(sum_element(num))

        return min(result)
