from .number_of_atoms import Solution


def test_count_of_atoms():
    assert Solution().countOfAtoms("H2O") == "H2O"
    assert Solution().countOfAtoms("Mg(OH)2") == "H2MgO2"
    assert Solution().countOfAtoms("K4(ON(SO3)2)2") == "K4N2O14S4"
