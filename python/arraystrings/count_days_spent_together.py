from typing import List


def calculate_day_of_year(day: str, prefix_sum: List[int]) -> int:
    month = int(day[:2])
    date = int(day[3:])
    return prefix_sum[month - 1] + date


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def count_days_together(
            arrive_alice: str, leave_alice: str, arrive_bob: str, leave_bob: str
    ) -> int:
        dates_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix_sum = [0]
        for date in dates_of_months:
            prefix_sum.append(prefix_sum[-1] + date)

        arrive_alice_day = calculate_day_of_year(arrive_alice, prefix_sum)
        leave_alice_day = calculate_day_of_year(leave_alice, prefix_sum)
        arrive_bob_day = calculate_day_of_year(arrive_bob, prefix_sum)
        leave_bob_day = calculate_day_of_year(leave_bob, prefix_sum)
        return max(
            0,
            min(leave_alice_day, leave_bob_day)
            - max(arrive_alice_day, arrive_bob_day)
            + 1,
        )
