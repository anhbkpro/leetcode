from typing import List


class Solution:
    @staticmethod
    def remove_interval(intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        def is_overlapping(current_interval: List[int], to_be_removed: List[int]) -> bool:
            if current_interval[0] < to_be_removed[1] and current_interval[1] > to_be_removed[0]:
                return True

            return False

        ans = []
        remove_start, remove_end = toBeRemoved
        for interval in intervals:
            # If there are no overlaps, add the interval to the list as is.
            if not is_overlapping(interval, toBeRemoved):
                ans.append(interval)
                continue

            start, end = interval
            # Is there a left interval we need to keep?
            if start < remove_start:
                ans.append([start, remove_start])

            # Is there a right interval we need to keep?
            if remove_end < end:
                ans.append([remove_end, end])

        return ans