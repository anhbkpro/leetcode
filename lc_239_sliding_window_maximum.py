from collections import deque
from typing import List


class Solution:
    @staticmethod
    def max_sliding_window(nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            print(f"=== Current index: {i}")
            if dq and dq[0] == i - k:
                print(f"\nPop out the first index {dq[0]} as its not in the range of current window.")
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                rightmost_element = dq.pop()
                print(f"Pop index {rightmost_element} as they have smaller corresponding.")

            dq.append(i)
            res.append(nums[dq[0]])

        return res
