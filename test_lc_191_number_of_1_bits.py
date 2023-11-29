from lc_191_number_of_1_bits import Solution


def test_hamming_weight():
    assert Solution.hammingWeight(n=0b00000000000000000000000000001011) == 3
    assert Solution.hammingWeight(n=0b00000000000000000000000010000000) == 1
