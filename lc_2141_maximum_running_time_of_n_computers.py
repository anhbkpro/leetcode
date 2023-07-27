from typing import List


class Solution:
    @staticmethod
    def maxRunTime(n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries) // n
        while left < right:
            target = right - (right - left) // 2
            if enough_power_run_all_computers(target, n, batteries):
                left = target
            else:
                right = target - 1

        return left


def enough_power_run_all_computers(mid: int, n: int, batteries: List[int]):
    extra = 0
    for power in batteries:
        extra += min(power, mid)

    return mid <= extra // n
