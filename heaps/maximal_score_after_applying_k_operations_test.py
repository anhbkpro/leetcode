from .maximal_score_after_applying_k_operations import Solution


def test_maximal_score_after_applying_k_operations():
    assert Solution().maxKelements(nums=[10, 10, 10, 10, 10], k=5) == 50
    assert Solution().maxKelements(nums=[1, 10, 3, 3, 3], k=3) == 17
