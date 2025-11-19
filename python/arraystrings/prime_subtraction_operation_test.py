from .prime_subtraction_operation import Solution


def test_prime_sub_operation():
    assert Solution().primeSubOperation(nums=[4, 9, 6, 10]) is True
    assert Solution().primeSubOperation(nums=[5, 8, 3]) is False
