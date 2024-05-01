from hashing.jewels_and_stones import Solution


def test_numJewelsInStones():
    assert Solution().numJewelsInStones("aA", "aAAbbbb") == 3
    assert Solution().numJewelsInStones("z", "ZZ") == 0
