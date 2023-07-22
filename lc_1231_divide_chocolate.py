from typing import List


def maximize_sweetness(sweetness: List[int], k: int) -> int:
    number_of_people = k + 1
    lo, hi = min(sweetness), sum(sweetness) // number_of_people
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if not_enough_cut(mid, sweetness, k):
            lo = mid
        else:
            hi = mid - 1

    return hi


class Solution:
    pass


def not_enough_cut(mid: int, sweetness: List[int], k: int):
    cur_sweetness = 0
    people_with_chocolate = 0
    for s in sweetness:
        cur_sweetness += s
        if cur_sweetness >= mid:
            cur_sweetness = 0
            people_with_chocolate += 1

    return people_with_chocolate >= k + 1
