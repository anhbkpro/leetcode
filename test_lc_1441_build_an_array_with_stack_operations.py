from lc_1441_build_an_array_with_stack_operations import Solution


def test_build_array():
    assert Solution.buildArray(target=[1, 3], n=3) == ["Push", "Push", "Pop", "Push"]
    assert Solution.buildArray(target=[1, 2, 3], n=3) == ["Push", "Push", "Push"]
    assert Solution.buildArray(target=[1, 2], n=4) == ["Push", "Push"]
