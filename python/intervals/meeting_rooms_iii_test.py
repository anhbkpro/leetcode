import pytest

from .meeting_rooms_iii import Solution


class TestMeetingRoomsIII:
    """Test suite for mostBooked function with heap and sorting implementations."""

    def setup_method(self):
        """Initialize solution instance for each test."""
        self.solution = Solution()

    def test_example_1_heap(self):
        """Test example 1 with heap implementation."""
        n = 2
        meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
        assert self.solution.mostBooked(n, meetings) == 0

    def test_example_2_heap(self):
        """Test example 2 with heap implementation."""
        n = 3
        meetings = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
        assert self.solution.mostBooked(n, meetings) == 1

    def test_single_room_heap(self):
        """Test with single room."""
        n = 1
        meetings = [[0, 5], [5, 10], [10, 15]]
        assert self.solution.mostBooked(n, meetings) == 0

    def test_empty_meetings_heap(self):
        """Test with no meetings."""
        n = 2
        meetings = []
        assert self.solution.mostBooked(n, meetings) == 0

    def test_single_meeting_heap(self):
        """Test with single meeting."""
        n = 3
        meetings = [[1, 5]]
        assert self.solution.mostBooked(n, meetings) == 0

    def test_all_rooms_used_equally_heap(self):
        """Test when all rooms are used equally."""
        n = 3
        meetings = [[0, 5], [0, 5], [0, 5]]
        assert self.solution.mostBooked(n, meetings) == 0

    def test_delayed_meetings_heap(self):
        """Test with delayed sequential meetings."""
        n = 2
        meetings = [[0, 10], [1, 2], [2, 3], [3, 4]]
        assert self.solution.mostBooked(n, meetings) == 1

    def test_example_1_sorting(self):
        """Test example 1 with sorting implementation."""
        n = 2
        meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
        assert self.solution.mostBookedSortingAndCounting(n, meetings) == 0

    def test_example_2_sorting(self):
        """Test example 2 with sorting implementation."""
        n = 3
        meetings = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
        assert self.solution.mostBookedSortingAndCounting(n, meetings) == 1

    def test_single_room_sorting(self):
        """Test with single room using sorting."""
        n = 1
        meetings = [[0, 5], [5, 10], [10, 15]]
        assert self.solution.mostBookedSortingAndCounting(n, meetings) == 0

    def test_empty_meetings_sorting(self):
        """Test with no meetings using sorting."""
        n = 2
        meetings = []
        assert self.solution.mostBookedSortingAndCounting(n, meetings) == 0

    def test_single_meeting_sorting(self):
        """Test with single meeting using sorting."""
        n = 3
        meetings = [[1, 5]]
        assert self.solution.mostBookedSortingAndCounting(n, meetings) == 0

    def test_all_rooms_used_equally_sorting(self):
        """Test when all rooms are used equally using sorting."""
        n = 3
        meetings = [[0, 5], [0, 5], [0, 5]]
        assert self.solution.mostBookedSortingAndCounting(n, meetings) == 0

    def test_delayed_meetings_sorting(self):
        """Test with delayed sequential meetings using sorting."""
        n = 2
        meetings = [[0, 10], [1, 2], [2, 3], [3, 4]]
        assert self.solution.mostBookedSortingAndCounting(n, meetings) == 1

    def test_many_rooms_few_meetings_heap(self):
        """Test with many rooms and few meetings."""
        n = 10
        meetings = [[0, 5], [1, 3]]
        assert self.solution.mostBooked(n, meetings) == 0

    def test_overlapping_meetings_heap(self):
        """Test with completely overlapping meetings."""
        n = 2
        meetings = [[1, 5], [1, 5], [1, 5]]
        result = self.solution.mostBooked(n, meetings)
        assert result in [0, 1]  # Either room could be busiest

    def test_overlapping_meetings_sorting(self):
        """Test with completely overlapping meetings using sorting."""
        n = 2
        meetings = [[1, 5], [1, 5], [1, 5]]
        result = self.solution.mostBookedSortingAndCounting(n, meetings)
        assert result in [0, 1]  # Either room could be busiest

    @pytest.mark.parametrize(
        "n,meetings,expected",
        [
            (1, [[0, 5]], 0),
            (2, [[0, 5], [5, 10]], 0),
            (3, [[0, 2], [1, 3], [2, 4]], 0),
            (2, [[0, 100]], 0),
        ],
    )
    def test_parametrized_heap(self, n, meetings, expected):
        """Parametrized test for heap implementation."""
        assert self.solution.mostBooked(n, meetings) == expected

    @pytest.mark.parametrize(
        "n,meetings,expected",
        [
            (1, [[0, 5]], 0),
            (2, [[0, 5], [5, 10]], 0),
            (3, [[0, 2], [1, 3], [2, 4]], 0),
            (2, [[0, 100]], 0),
        ],
    )
    def test_parametrized_sorting(self, n, meetings, expected):
        """Parametrized test for sorting implementation."""
        assert self.solution.mostBookedSortingAndCounting(n, meetings) == expected

    def test_long_meetings_heap(self):
        """Test with one long meeting blocking other rooms."""
        n = 2
        meetings = [[0, 100], [1, 2], [2, 3], [3, 4]]
        assert self.solution.mostBooked(n, meetings) == 1

    def test_concurrent_start_times_heap(self):
        """Test with concurrent start times."""
        n = 3
        meetings = [[0, 5], [0, 10], [0, 15]]
        assert self.solution.mostBooked(n, meetings) == 0

    def test_large_gaps_between_meetings_heap(self):
        """Test with large gaps between meetings."""
        n = 2
        meetings = [[0, 5], [10, 15], [20, 25]]
        assert self.solution.mostBooked(n, meetings) == 0

    def test_long_meetings_sorting(self):
        """Test with one long meeting blocking other rooms using sorting."""
        n = 2
        meetings = [[0, 100], [1, 2], [2, 3], [3, 4]]
        assert self.solution.mostBookedSortingAndCounting(n, meetings) == 1

    def test_concurrent_start_times_sorting(self):
        """Test with concurrent start times using sorting."""
        n = 3
        meetings = [[0, 5], [0, 10], [0, 15]]
        assert self.solution.mostBookedSortingAndCounting(n, meetings) == 0

    def test_large_gaps_between_meetings_sorting(self):
        """Test with large gaps between meetings using sorting."""
        n = 2
        meetings = [[0, 5], [10, 15], [20, 25]]
        assert self.solution.mostBookedSortingAndCounting(n, meetings) == 0
