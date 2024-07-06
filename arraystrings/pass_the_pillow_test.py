from .pass_the_pillow import Solution


def test_pass_the_pillow():
    assert Solution().passThePillow(n = 4, time = 5) == 2
    assert Solution().passThePillow(n = 3, time = 2) == 3
