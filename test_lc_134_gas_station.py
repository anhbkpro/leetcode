from lc_134_gas_station import Solution


def test_can_complete_circuit():
    assert Solution.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]) == 3
    assert Solution.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]) == -1
