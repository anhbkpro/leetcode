from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        matched_indexes = [i for i in range(len(nums)) if nums[i] == key]
        ans = []
        for i in range(len(nums)):
            for t in matched_indexes:
                if abs(i - t) <= k:
                    ans.append(i)

        return sorted(list(set(ans)))
