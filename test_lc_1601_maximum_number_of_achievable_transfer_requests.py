from lc_1601_maximum_number_of_achievable_transfer_requests import maximumRequests


def test_maximum_requests():
    assert maximumRequests(5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]) == 5
    assert maximumRequests(3, [[0, 0], [1, 2], [2, 1]]) == 3
    assert maximumRequests(4, [[0, 3], [3, 1], [1, 2], [2, 0]]) == 4
