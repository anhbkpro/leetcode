from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        merged = []
        for start, end in intervals:
            # not intersect
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            # intersect
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged
