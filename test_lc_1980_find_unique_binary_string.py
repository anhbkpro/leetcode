from lc_1980_find_unique_binary_string import Solution


def test_find_different_binary_string():
    assert Solution.findDifferentBinaryString(nums=["01", "10"]) in ["00", "11"]
    assert Solution.findDifferentBinaryString(nums=["00", "01"]) in ["10", "11"]
