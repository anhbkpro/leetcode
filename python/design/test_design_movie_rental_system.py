import unittest

from .design_movie_rental_system import MovieRentingSystem


class TestMovieRentingSystem(unittest.TestCase):
    def setUp(self):
        # Example from the prompt
        self.entries = [
            [0, 1, 5],
            [0, 2, 6],
            [0, 3, 7],
            [1, 1, 4],
            [1, 2, 7],
            [2, 1, 5],
        ]
        self.system = MovieRentingSystem(3, self.entries)

    def test_full_flow(self):
        # search(1) -> [1, 0, 2]
        self.assertEqual(self.system.search(1), [1, 0, 2])
        # rent(0, 1)
        self.system.rent(0, 1)
        # rent(1, 2)
        self.system.rent(1, 2)
        # report() -> [[0, 1], [1, 2]]
        self.assertEqual(self.system.report(), [[0, 1], [1, 2]])
        # drop(1, 2)
        self.system.drop(1, 2)
        # search(2) -> [0, 1]
        self.assertEqual(self.system.search(2), [0, 1])

    def test_search_empty(self):
        # search for a movie not in the system
        self.assertEqual(self.system.search(999), [])

    def test_report_empty(self):
        # No movies rented yet
        self.assertEqual(self.system.report(), [])

    def test_rent_and_drop(self):
        self.system.rent(0, 2)
        self.assertEqual(self.system.report(), [[0, 2]])
        self.system.drop(0, 2)
        self.assertEqual(self.system.report(), [])

    def test_report_tiebreakers(self):
        # Rent all movies with price 5
        self.system.rent(0, 1)  # price 5
        self.system.rent(2, 1)  # price 5
        # Both have price 5, shop 0 < shop 2, so order is [[0,1],[2,1]]
        self.assertEqual(self.system.report(), [[0, 1], [2, 1]])


if __name__ == "__main__":
    unittest.main()
