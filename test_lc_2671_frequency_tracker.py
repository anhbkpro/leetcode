from lc_2671_frequency_tracker import FrequencyTracker

ft = FrequencyTracker()


def test_frequency_tracker():
    ft.add(3)
    ft.add(3)
    if not ft.hasFrequency(2):
        assert False
