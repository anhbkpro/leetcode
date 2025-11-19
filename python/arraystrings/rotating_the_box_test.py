from .rotating_the_box import Solution


def test_rotate_the_box():
    assert Solution().rotateTheBox(box=[["#", ".", "#"]]) == [["."], ["#"], ["#"]]
    assert Solution().rotateTheBox(
        box=[["#", ".", "*", "."], ["#", "#", "*", "."]]
    ) == [["#", "."], ["#", "#"], ["*", "*"], [".", "."]]
