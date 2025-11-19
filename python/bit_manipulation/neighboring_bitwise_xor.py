from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        sum = 0
        for num in derived:
            sum ^= num

        return not sum
