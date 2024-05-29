from simulation.number_of_steps_to_reduce_a_number_in_binary_representation_to_one import Solution


def test_number_of_steps():
    assert Solution().numSteps("1101") == 6
    assert Solution().numSteps("10") == 1
