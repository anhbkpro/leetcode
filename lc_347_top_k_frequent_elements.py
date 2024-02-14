from collections import Counter
from typing import List
import heapq


class Solution:
    @staticmethod
    def top_k_frequent(nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements.
        :param nums: 1 <= nums.length <= 10^5, -10^4 <= nums[i] <= 10^4
        :param k: k is in the range [1, the number of unique elements in the array]
        :return: k most frequent elements
        """
        # O(1) time
        if k == len(nums):
            return nums

        # 1. Build hash map: character and how often it appears
        # O(N) time
        count = Counter(nums)
        # 2-3. Build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)
