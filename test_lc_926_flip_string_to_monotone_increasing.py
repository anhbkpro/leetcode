from lc_926_flip_string_to_monotone_increasing import minFlipsMonoIncr


def test_min_flips_mono_incr():
    assert minFlipsMonoIncr("00110") == 1
    assert minFlipsMonoIncr("010110") == 2
    assert minFlipsMonoIncr("00011000") == 2
