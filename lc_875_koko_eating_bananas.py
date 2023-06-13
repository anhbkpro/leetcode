from typing import List


def possible(speed: int, piles: List[int], h: int) -> bool:
    # print(f"--- Koko is eating with speed: {speed}")
    total_hours_needed = 0
    for pile in piles:
        total_hours_needed += (pile + speed - 1) // speed  # could be math.ceil(pile / speed)
        # print(f"Hour(s) needed to eat a pile of {pile} bananas: {total_hours_needed}")
    return total_hours_needed <= h


def min_eating_speed(piles: List[int], h: int) -> int:
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if possible(mid, piles, h):
            hi = mid
        else:
            lo = mid + 1
    return lo


class Solution:
    pass
