import unittest
from .maximum_number_of_tasks_you_can_assign import Solution


class TestMaximumNumberOfTasksYouCanAssign(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_typical_case(self):
        tasks = [3, 2, 1]
        workers = [0, 3, 3]
        pills = 1
        strength = 1
        # Assignments: worker 1 (0+1) can do task 1, worker 2 (3) can do task 2, worker 3 (3) can do task 3
        self.assertEqual(
            self.solution.maxTaskAssign(tasks, workers, pills, strength), 3
        )


if __name__ == "__main__":
    unittest.main()
