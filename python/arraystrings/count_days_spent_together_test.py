from typing import List

from .count_days_spent_together import Solution, calculate_day_of_year

DAYS_IN_MONTHS: List[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def build_prefix_sum() -> List[int]:
    prefix_sum: List[int] = [0]
    for days in DAYS_IN_MONTHS:
        prefix_sum.append(prefix_sum[-1] + days)
    return prefix_sum


def test_count_days_together_when_stays_partially_overlap() -> None:
    input_arrive_alice: str = "08-15"
    input_leave_alice: str = "08-18"
    input_arrive_bob: str = "08-16"
    input_leave_bob: str = "08-19"
    expected_days: int = 3

    actual_days: int = Solution().count_days_together(
        input_arrive_alice, input_leave_alice, input_arrive_bob, input_leave_bob
    )

    assert actual_days == expected_days


def test_count_days_together_when_stays_do_not_overlap() -> None:
    input_arrive_alice: str = "10-01"
    input_leave_alice: str = "10-31"
    input_arrive_bob: str = "11-01"
    input_leave_bob: str = "12-31"
    expected_days: int = 0

    actual_days: int = Solution().count_days_together(
        input_arrive_alice, input_leave_alice, input_arrive_bob, input_leave_bob
    )

    assert actual_days == expected_days


def test_count_days_together_when_both_stay_the_same_single_day() -> None:
    input_arrive_alice: str = "01-01"
    input_leave_alice: str = "01-01"
    input_arrive_bob: str = "01-01"
    input_leave_bob: str = "01-01"
    expected_days: int = 1

    actual_days: int = Solution().count_days_together(
        input_arrive_alice, input_leave_alice, input_arrive_bob, input_leave_bob
    )

    assert actual_days == expected_days


def test_count_days_together_when_one_stay_contains_the_other() -> None:
    input_arrive_alice: str = "01-01"
    input_leave_alice: str = "12-31"
    input_arrive_bob: str = "03-01"
    input_leave_bob: str = "03-31"
    expected_days: int = 31

    actual_days: int = Solution().count_days_together(
        input_arrive_alice, input_leave_alice, input_arrive_bob, input_leave_bob
    )

    assert actual_days == expected_days


def test_count_days_together_when_stays_touch_on_one_day() -> None:
    input_arrive_alice: str = "02-01"
    input_leave_alice: str = "02-28"
    input_arrive_bob: str = "02-28"
    input_leave_bob: str = "03-05"
    expected_days: int = 1

    actual_days: int = Solution().count_days_together(
        input_arrive_alice, input_leave_alice, input_arrive_bob, input_leave_bob
    )

    assert actual_days == expected_days


def test_count_days_together_when_overlap_spans_months() -> None:
    input_arrive_alice: str = "01-25"
    input_leave_alice: str = "03-10"
    input_arrive_bob: str = "02-20"
    input_leave_bob: str = "04-01"
    expected_days: int = 19

    actual_days: int = Solution().count_days_together(
        input_arrive_alice, input_leave_alice, input_arrive_bob, input_leave_bob
    )

    assert actual_days == expected_days


def test_calculate_day_of_year_when_first_day_of_year() -> None:
    input_day: str = "01-01"
    input_prefix_sum: List[int] = build_prefix_sum()
    expected_day_of_year: int = 1

    actual_day_of_year: int = calculate_day_of_year(input_day, input_prefix_sum)

    assert actual_day_of_year == expected_day_of_year


def test_calculate_day_of_year_when_first_day_after_february() -> None:
    input_day: str = "03-01"
    input_prefix_sum: List[int] = build_prefix_sum()
    expected_day_of_year: int = 60

    actual_day_of_year: int = calculate_day_of_year(input_day, input_prefix_sum)

    assert actual_day_of_year == expected_day_of_year


def test_calculate_day_of_year_when_last_day_of_year() -> None:
    input_day: str = "12-31"
    input_prefix_sum: List[int] = build_prefix_sum()
    expected_day_of_year: int = 365

    actual_day_of_year: int = calculate_day_of_year(input_day, input_prefix_sum)

    assert actual_day_of_year == expected_day_of_year
