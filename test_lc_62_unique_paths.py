from lc_62_unique_paths import unique_paths


def test_unique_paths():
    assert unique_paths(m=3, n=2) == 3
    assert unique_paths(m=7, n=3) == 28
