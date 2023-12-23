from lc_1496_path_crossing import Solution


def test_is_path_crossing():
    assert Solution.isPathCrossing(path="NES") is False
    assert Solution.isPathCrossing(path="NESWW") is True
