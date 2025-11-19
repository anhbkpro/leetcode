from .find_the_student_that_will_replace_the_chalk import Solution


def test_chalk_replacer():
    assert Solution().chalkReplacer([5, 1, 5], 22) == 0
    assert Solution().chalkReplacer([3, 4, 1, 2], 25) == 1
