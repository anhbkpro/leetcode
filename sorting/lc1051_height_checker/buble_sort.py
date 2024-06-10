from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        def bubble_sort():
            n = len(sorted_heights)
            for i in range(n - 1):
                for j in range(n - i - 1):
                    if sorted_heights[j] > sorted_heights[j + 1]:
                        sorted_heights[j], sorted_heights[j + 1] = sorted_heights[j + 1], sorted_heights[j]

        sorted_heights = heights[:]
        bubble_sort()

        count = 0
        for i in range(len(heights)):
            count += sorted_heights[i] != heights[i]

        return count
