from unittest import TestCase
from lc_837_new_21_game import new21Game


class TestSolution(TestCase):
    def test_new21game(self):
        self.assertAlmostEqual(new21Game(n=10, k=1, maxPts=10), 1.0)
        self.assertAlmostEqual(new21Game(n=6, k=1, maxPts=10), 0.6)
        self.assertAlmostEqual(new21Game(n=21, k=17, maxPts=10), 0.73278, 5)
