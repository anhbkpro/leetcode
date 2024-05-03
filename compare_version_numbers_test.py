from compare_version_numbers import Solution


def test_compare_version_numbers():
    assert Solution().compareVersion("1.01", "1.001") == 0
    assert Solution().compareVersion("1.0", "1.0.0") == 0
    assert Solution().compareVersion("0.1", "1.1") == -1
