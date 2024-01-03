from lc_2125_number_of_laser_beams_in_a_bank import Solution


def test_number_of_beams():
    assert Solution().numberOfBeams(bank=["011001", "000000", "010100", "001000"]) == 8
    assert Solution().numberOfBeams(bank=["000", "111", "000"]) == 0
