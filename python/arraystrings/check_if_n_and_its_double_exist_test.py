from .check_if_n_and_its_double_exist import Solution


def test_check_if_double_exist():
    assert Solution().checkIfExist([10, 2, 5, 3])
    assert Solution().checkIfExist([7, 1, 14, 11])
    assert not Solution().checkIfExist([3, 1, 7, 11])
