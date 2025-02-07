from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """Insert a new interval into a list of non-overlapping sorted intervals.

        Args:
            intervals: A list of non-overlapping intervals sorted by start time.
            newInterval: A new interval to be inserted.

        Returns:
            A new list of non-overlapping intervals sorted by start time.

        Time complexity: O(n) where n is the number of intervals
        Space complexity: O(n) for the result list
        """
        result = []
        i = 0
        n = len(intervals)

        # Add all intervals that come before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged interval
        result.append(newInterval)

        # Add remaining intervals
        result.extend(intervals[i:])

        return result
