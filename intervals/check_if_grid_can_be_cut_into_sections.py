from typing import List


class Solution:
    def merge_intervals(self, intervals):
        """
        Merge overlapping intervals.

        Args:
            intervals: List of [start, end] intervals

        Returns:
            List of merged intervals
        """
        if not intervals:
            return []

        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for current in intervals[1:]:
            previous = merged[-1]

            # If current interval overlaps with or is adjacent to the previous one
            if current[0] < previous[1]:
                # Update the end of previous interval if needed
                previous[1] = max(previous[1], current[1])
            else:
                # If no overlap, add the current interval to the result
                merged.append(current)

        return merged

    def extract_dimension_intervals(self, rectangles, horizontal=True):
        """
        Extract intervals for a specific dimension from the rectangles.

        Args:
            rectangles: List of [x1, y1, x2, y2] rectangles
            horizontal: If True, extract x-intervals, otherwise y-intervals

        Returns:
            List of [start, end] intervals for the specified dimension
        """
        if horizontal:
            return [[rec[0], rec[2]] for rec in rectangles]
        else:
            return [[rec[1], rec[3]] for rec in rectangles]

    def has_valid_cuts(self, intervals):
        """
        Check if there are at least 3 non-overlapping segments after merging.

        Args:
            intervals: List of [start, end] intervals

        Returns:
            True if there are at least 3 merged intervals, False otherwise
        """
        merged = self.merge_intervals(intervals)
        return len(merged) >= 3

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        """
        Check if the rectangles can be cut horizontally or vertically.

        Args:
            n: Number of rectangles
            rectangles: List of [x1, y1, x2, y2] rectangles

        Returns:
            True if valid cuts exist, False otherwise
        """
        # Extract intervals for horizontal and vertical dimensions
        horizontal_intervals = self.extract_dimension_intervals(
            rectangles, horizontal=True
        )
        vertical_intervals = self.extract_dimension_intervals(
            rectangles, horizontal=False
        )

        # Check if either dimension has valid cuts
        return self.has_valid_cuts(horizontal_intervals) or self.has_valid_cuts(
            vertical_intervals
        )
