from typing import List


# My solution:
class Solution:
    @staticmethod
    def groupThePeople(groupSizes: List[int]) -> List[List[int]]:
        bucket = {}
        n = len(groupSizes)
        for idx in range(n):
            if groupSizes[idx] in bucket:
                bucket[groupSizes[idx]].append(idx)
            else:
                bucket[groupSizes[idx]] = [idx]

        ans = []
        for k in bucket:
            number_of_iterable = len(bucket[k]) // k
            for i in range(number_of_iterable):
                ans.append(bucket[k][i * k: (i + 1) * k])

        return ans
