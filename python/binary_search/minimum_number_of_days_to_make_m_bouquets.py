from typing import List


class Solution:
    def get_num_of_bouquets(self, bloomDay: List[int], mid: int, k: int) -> int:
        bouquets = 0
        flowers = 0
        for day in bloomDay:
            if day <= mid:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left = 1
        right = max(bloomDay)
        minDays = -1
        while left <= right:
            mid = (left + right) // 2
            if self.get_num_of_bouquets(bloomDay, mid, k) >= m:
                minDays = mid
                right = mid - 1
            else:
                left = mid + 1

        return minDays
