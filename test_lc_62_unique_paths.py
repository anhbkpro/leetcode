from lc_62_unique_paths import unique_paths, Solution


def test_unique_paths():
    assert unique_paths(m=3, n=2) == 3
    assert unique_paths(m=7, n=3) == 28


def test_unique_paths_spaced_optimized():
    assert Solution.unique_paths_spaced_optimized(m=3, n=2) == 3
    assert Solution.unique_paths_spaced_optimized(m=7, n=3) == 28
