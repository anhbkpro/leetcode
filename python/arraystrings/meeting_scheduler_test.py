from .meeting_scheduler import Solution


def test_min_available_duration():
    assert Solution().minAvailableDuration(
        [[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8
    ) == [60, 68]
    assert (
        Solution().minAvailableDuration(
            [[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12
        )
        == []
    )
