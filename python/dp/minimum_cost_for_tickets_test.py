import unittest

from dp.minimum_cost_for_tickets import SolutionTopDownDP


class TestMinCostTickets(unittest.TestCase):
    def setUp(self):
        self.solution = SolutionTopDownDP()

    def test_basic_case(self):
        """Test with basic example having obvious minimum cost path"""
        days = [1, 4, 6, 7, 8, 20]
        costs = [2, 7, 15]
        self.assertEqual(self.solution.mincostTickets(days, costs), 11)
        # Explanation: Buy a 1-day pass on days 1, 4, 6, 7, 8 for $2 each, and a 1-day pass on day 20 for $2.
        # Total cost = 2*6 = $11

    def test_seven_day_pass_better(self):
        """Test when 7-day pass is more economical"""
        days = [1, 2, 3, 4, 5, 6, 7]
        costs = [7, 10, 25]
        self.assertEqual(self.solution.mincostTickets(days, costs), 10)
        # Explanation: Buy a 7-day pass for $10 instead of seven 1-day passes for $49

    def test_thirty_day_pass_better(self):
        """Test when 30-day pass is more economical"""
        days = [1, 5, 10, 15, 20, 25, 30]
        costs = [10, 20, 25]
        self.assertEqual(self.solution.mincostTickets(days, costs), 25)
        # Explanation: Buy a 30-day pass for $25 instead of multiple shorter passes

    def test_single_day(self):
        """Test with just one travel day"""
        days = [1]
        costs = [2, 7, 15]
        self.assertEqual(self.solution.mincostTickets(days, costs), 2)
        # Explanation: Only need one 1-day pass

    def test_consecutive_days(self):
        """Test with many consecutive travel days"""
        days = list(range(1, 11))  # 1 to 10
        costs = [1, 5, 20]
        self.assertEqual(self.solution.mincostTickets(days, costs), 8)
        # Explanation: A 7-day pass for $5 + 3 1-day passes for $1 each (= $8 total) is cheaper than 10 1-day passes

    def test_scattered_days(self):
        """Test with scattered travel days"""
        days = [1, 10, 20, 30]
        costs = [2, 7, 15]
        self.assertEqual(self.solution.mincostTickets(days, costs), 8)
        # Explanation: Buy 4 single-day passes

    def test_end_of_year(self):
        """Test with travel days at the end of year"""
        days = [355, 360, 365]
        costs = [3, 7, 20]
        self.assertEqual(self.solution.mincostTickets(days, costs), 9)
        # Explanation: Buy 3 1-day pass for $3 each = $9

    def test_expensive_daily_pass(self):
        """Test when daily passes are more expensive than longer duration passes"""
        days = [1, 2, 3]
        costs = [10, 5, 8]
        self.assertEqual(self.solution.mincostTickets(days, costs), 5)
        # Explanation: 7-day pass is cheaper than 3 daily passes

    def test_edge_case_single_day_large_gap(self):
        """Test with large gaps between travel days"""
        days = [1, 50, 100]
        costs = [3, 7, 20]
        self.assertEqual(self.solution.mincostTickets(days, costs), 9)
        # Explanation: Three single-day passes are optimal due to large gaps


if __name__ == "__main__":
    unittest.main()
