from bisect import bisect


class Solution:
    @staticmethod
    def insert(intervals, newInterval):
        # O(logN)
        position = bisect(intervals, newInterval)
        # O(N)
        intervals.insert(position, newInterval)

        merged = []
        # O(N)
        for start, end in intervals:
            # if the list of merged intervals is empty or if the current interval does not overlap with the previous,
            # simply append it.
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                # otherwise, there is overlap, so we merge the current and previous intervals by updating the end of
                # the previous interval if it is less than the end of the current interval.
                merged[-1][1] = max(merged[-1][1], end)

        return merged
