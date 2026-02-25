from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def find_weight(num):
            weight = 0

            while num:
                # 👉 number of loops = number of 1 bits.
                weight += 1
                num &= (num - 1) # removes the rightmost 1 bit -> very efficient.

            return weight

        arr.sort(key = lambda num: (find_weight(num), num)) # sorts tuples lexicographically -> first by weight, then by value.
        return arr
