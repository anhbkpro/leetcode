import heapq
from typing import List


class Solution:
    @staticmethod
    def k_weakest_rows(mat: List[List[int]], k: int) -> List[int]:

        m = len(mat)
        n = len(mat[0])

        def binary_search(row):
            low = 0
            high = n
            while low < high:
                mid = low + (high - low) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low

        # Calculate the strength of each row using binary search.
        # Put the strength/index pairs into a priority queue.
        pq = []
        for i, row in enumerate(mat):
            strength = binary_search(row)
            entry = (-strength, -i)
            if len(pq) < k or entry > pq[0]:
                heapq.heappush(pq, entry)
            if len(pq) > k:
                heapq.heappop(pq)

        # Pull out and return the indexes of the smallest k entries.
        # Don't forget to convert them back to positive numbers!
        indexes = []
        while pq:
            strength, i = heapq.heappop(pq)
            indexes.append(-i)

        # Reverse, as the indexes are around the wrong way.
        indexes = indexes[::-1]

        return indexes

    @staticmethod
    def k_weakest_rows_nsmallest(mat: List[List[int]], k: int) -> List[int]:
        def number_of_soldiers(row: List[int]) -> int:
            lo, hi = 0, len(row) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if not row[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            return lo

        soldier_freq = {idx: number_of_soldiers(row) for idx, row in enumerate(mat)}
        return heapq.nsmallest(k, soldier_freq.keys(), key=soldier_freq.get)
