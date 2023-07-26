from math import ceil
from typing import List


class Solution:
    @staticmethod
    def min_speed_on_time(dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1  # Impossible to arrive on time.

        upper = 10000000
        lo, hi = 1, upper
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_arrive_on_time(mid, dist, hour):
                hi = mid - 1
            else:
                lo = mid + 1

        if lo > upper:
            return -1  # Impossible to arrive on time.

        return lo


def can_arrive_on_time(speed: int, dist: List[int], hour: float) -> bool:
    time_required = 0
    for train in dist:
        time_required += ceil(train / speed)

    # Round off to the next integer, if not the last ride.
    time_required = time_required - ceil(dist[-1] / speed) + dist[-1] / speed

    return time_required <= hour
