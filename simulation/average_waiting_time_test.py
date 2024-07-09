from .average_waiting_time import Solution


def test_average_waiting_time():
    assert Solution().averageWaitingTime(customers=[[1, 2], [2, 5], [4, 3]]) == 5.0
    assert Solution().averageWaitingTime(customers=[[5, 2], [5, 4], [10, 3], [20, 1]]) == 3.25
