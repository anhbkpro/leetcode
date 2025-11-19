from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        f1 = Counter(arr1)
        f2 = Counter(arr2)
        remaining = []
        for num in arr2:
            ans.extend([num] * f1[num])

        visited = set()
        for num in arr1:
            if num in f2 or num in visited:
                continue
            remaining.extend([num] * f1[num])
            visited.add(num)

        remaining.sort()
        ans.extend(remaining)
        return ans
