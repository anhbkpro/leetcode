from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        m = {}
        for i in range(len(arr)):
            if 2 * arr[i] in m and m[2 * arr[i]] != i:
                return True
            d = arr[i] // 2
            if d in m and 2 * d == arr[i] and m[d] != i:
                return True
            m[arr[i]] = i

        return False
