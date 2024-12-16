from .final_array_state_after_k_multiplication_operations_i import Solution


def test_get_final_state():
    assert Solution().getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2) == [
        8,
        4,
        6,
        5,
        6,
    ]
    assert Solution().getFinalState(nums=[1, 2], k=3, multiplier=4) == [16, 8]
