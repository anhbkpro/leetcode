import functools
from typing import List


class Solution:
    @staticmethod
    def combinationSum4(nums: List[int], target: int) -> int:
        # potential optimization
        # nums.sort()

        @functools.lru_cache(maxsize=None)
        def combs(remain):
            if remain == 0:
                return 1

            result = 0
            for num in nums:
                if remain - num >= 0:
                    result += combs(remain - num)
                # potential optimization
                # else:
                #     break

            return result

        return combs(target)
