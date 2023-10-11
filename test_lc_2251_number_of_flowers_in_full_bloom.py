from lc_2251_number_of_flowers_in_full_bloom import Solution


def test_full_bloom_flowers():
    assert Solution.fullBloomFlowers(flowers=[[1, 6], [3, 7], [9, 12], [4, 13]], people=[2, 3, 7, 11]) == [1, 2, 2, 2]
    assert Solution.fullBloomFlowers(flowers=[[1, 10], [3, 3]], people=[3, 3, 2]) == [2, 2, 1]
