from heaps.k_th_smallest_prime_fraction import Solution


def test_k_th_smallest_prime_fraction():
    assert Solution().kthSmallestPrimeFraction([1, 2, 3, 5], 3) == [2, 5]
