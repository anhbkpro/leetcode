from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)
        # O(NlogN), this can be optimized to O(logN) by using binary search (insert_interval_use_binary_search.py)
        intervals.sort(key=lambda x: x[0])  # O(NlogN)

        ans = []
        for start, end in intervals:
            # not intersect
            if end < newInterval[0] or start > newInterval[1]:
                ans.append([start, end])
                continue

            # intersect
            if ans and ans[-1][1] >= start:
                start = min(ans[-1][0], start)
                end = max(ans[-1][1], end)
                ans = ans[:-1]

            to_be_inserted_interval = [
                min(start, newInterval[0]),
                max(end, newInterval[1]),
            ]
            ans.append(to_be_inserted_interval)

        return ans
