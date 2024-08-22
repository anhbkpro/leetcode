from .number_complement import Solution

def test_number_complement():
    assert Solution().findComplement(5) == 2
    assert Solution().findComplement(1) == 0
