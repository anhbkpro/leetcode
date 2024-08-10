from dfs.number_of_spaces_cleaning_robot_cleaned import Solution


def test_number_of_spaces_cleaning_robot_cleaned():
    assert Solution().numberOfCleanRooms(room=[[0, 0, 0], [1, 1, 0], [0, 0, 0]]) == 7
    assert Solution().numberOfCleanRooms(room=[[0, 1, 0], [1, 0, 0], [0, 0, 0]]) == 1
