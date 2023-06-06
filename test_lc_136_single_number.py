from lc_136_single_number import SolutionBitManipulation

bm = SolutionBitManipulation()


def test_single_number():
    assert bm.singleNumber(nums=[2, 2, 1]) == 1
