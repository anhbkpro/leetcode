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
            if not is_overlapping(interval, toBeRemoved):
                ans.append(interval)
                continue

            start, end = interval
            if start < remove_start:
                ans.append([start, min(remove_start, end)])

            if remove_end < end:
                ans.append([max(remove_end, start), end])

        return ans