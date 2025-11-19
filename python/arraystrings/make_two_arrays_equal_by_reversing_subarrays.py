from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Dictionary to maintain frequency count for arr
        arrFreq = self._build_dict(arr)
        targetFreq = self._build_dict(target)

        # Number of distinct elements of the 2 arrays are not equal
        if len(arrFreq) != len(targetFreq):
            return False

        for key in arrFreq:
            # Frequency for num differs
            if arrFreq[key] != targetFreq.get(key, 0):
                return False

        return True

    def _build_dict(self, arr: List[int]) -> dict:
        freq = {}
        for num in arr:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        return freq
