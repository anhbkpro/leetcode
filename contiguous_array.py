from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        count = 0
        max_len = 0
        for i, num in enumerate(nums):
            # update the sum,
            # decrement by 1 for 0
            # and increase by 1 for 1
            count += 1 if num == 1 else -1
            # If the sum becomes zero at any index,
            # update the maximum length to the current index plus one.
            if count == 0:
                # i = 1 => max_len = 2
                # i = 5 => max_len = 6
                max_len = i + 1
            elif count in mp:
                # i = 2 => max_len = 2
                # i = 4 => max_len = 4
                max_len = max(max_len, i - mp[count])
            else:
                mp[count] = i
                # i = 0: mp[-1] = 0
                # i = 3: mp[-2] = 3

        return max_len
