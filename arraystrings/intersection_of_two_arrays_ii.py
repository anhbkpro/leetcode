from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        ans = []
        for k in counter1:
            if k in counter2:
                ans = ans + ([k] * min(counter1[k], counter2[k]))

        return ans
