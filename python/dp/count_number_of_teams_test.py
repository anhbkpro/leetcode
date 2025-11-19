from .count_number_of_teams import Solution


def test_num_teams():
    assert Solution().numTeams([2, 5, 3, 4, 1]) == 3
    assert Solution().numTeams([2, 1, 3]) == 0
