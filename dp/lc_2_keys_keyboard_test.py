from .lc_2_keys_keyboard import Solution


def test_min_steps():
    assert Solution().minSteps(3) == 3
    assert Solution().minSteps(1) == 0
