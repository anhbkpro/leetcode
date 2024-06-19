from .minimum_number_of_days_to_make_m_bouquets import Solution


def test_minimum_number_of_days_to_make_m_bouquets():
    assert Solution().minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1) == 3
    assert Solution().minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=2) == -1
