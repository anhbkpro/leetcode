import heapq
from typing import List


class Solution:
    @staticmethod
    def find_kth_largest(nums: List[int], k: int) -> int:
        """
        Given an integer array nums and an integer k, return the kth largest element in the array.
        Note that it is the kth largest element in the sorted order, not the kth distinct element.
        :param nums: 1 <= nums.length <= 10^5, -10^4 <= nums[i] <= 10^4
        :param k: 1 <= k <= nums.length
        :return: kth largest element in the array
        Input 1: nums = [3,2,1,5,6,4], k = 2
        Output: 5
        Explanation: The sorted nums are [6,5,4,3,2,1]. The 2nd largest number is 5.

        Input 2: nums = [3,2,3,1,2,4,5,5,6], k = 4
        Output: 4
        Explanation: The sorted nums are [6,5,5,4,3,3,2,2,1]. The 4th largest number is 4.
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
