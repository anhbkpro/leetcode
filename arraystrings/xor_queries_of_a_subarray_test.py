from .xor_queries_of_a_subarray import Solution


def test_xor_queries():
    assert Solution().xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]) == [2, 7, 14, 8]
