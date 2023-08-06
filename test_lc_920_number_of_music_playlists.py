from lc_920_number_of_music_playlists import Solution


def test_num_music_playlists():
    assert Solution.numMusicPlaylists(3, 3, 1) == 6
    assert Solution.numMusicPlaylists(2, 3, 0) == 6
    assert Solution.numMusicPlaylists(2, 3, 1) == 2
