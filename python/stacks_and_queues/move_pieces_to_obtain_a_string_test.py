from .move_pieces_to_obtain_a_string import Solution


def test_min_operations():
    assert Solution().canChange(start="_L__R__R_", target="L______RR") is True
    assert Solution().canChange(start="_R", target="R_") is False
