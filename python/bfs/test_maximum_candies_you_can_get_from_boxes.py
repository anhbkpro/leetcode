import unittest

from .maximum_candies_you_can_get_from_boxes import Solution


class TestMaximumCandies(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_input(self):
        self.assertEqual(self.solution.maxCandies([], [], [], [], []), 0)

    def test_single_box(self):
        # Test case with one box that is initially open
        self.assertEqual(
            self.solution.maxCandies(
                status=[1],
                candies=[5],
                keys=[[]],
                containedBoxes=[[]],
                initialBoxes=[0],
            ),
            5,
        )

        # Test case with one box that is initially closed
        self.assertEqual(
            self.solution.maxCandies(
                status=[0],
                candies=[5],
                keys=[[]],
                containedBoxes=[[]],
                initialBoxes=[0],
            ),
            0,
        )

    def test_multiple_boxes_no_keys(self):
        # Test case with multiple boxes, all initially open
        self.assertEqual(
            self.solution.maxCandies(
                status=[1, 1, 1],
                candies=[1, 2, 3],
                keys=[[], [], []],
                containedBoxes=[[], [], []],
                initialBoxes=[0, 1, 2],
            ),
            6,
        )

        # Test case with multiple boxes, some initially closed
        self.assertEqual(
            self.solution.maxCandies(
                status=[1, 0, 1],
                candies=[1, 2, 3],
                keys=[[], [], []],
                containedBoxes=[[], [], []],
                initialBoxes=[0, 1, 2],
            ),
            4,
        )

    def test_boxes_with_keys(self):
        # Test case where keys are found in boxes
        self.assertEqual(
            self.solution.maxCandies(
                status=[1, 0, 0],
                candies=[1, 2, 3],
                keys=[[1], [], []],
                containedBoxes=[[1], [], []],
                initialBoxes=[0],
            ),
            3,
        )

        # Test case with multiple keys
        self.assertEqual(
            self.solution.maxCandies(
                status=[1, 0, 0, 0],
                candies=[1, 2, 3, 4],
                keys=[[1], [2], [3], []],
                containedBoxes=[[], [], [], []],
                initialBoxes=[0],
            ),
            1,
        )

    def test_boxes_with_contained_boxes(self):
        # Test case with boxes containing other boxes
        self.assertEqual(
            self.solution.maxCandies(
                status=[1, 1, 0],
                candies=[1, 2, 3],
                keys=[[], [], []],
                containedBoxes=[[1], [2], []],
                initialBoxes=[0],
            ),
            3,
        )

        # Test case with nested boxes and keys
        self.assertEqual(
            self.solution.maxCandies(
                status=[1, 0, 0],
                candies=[1, 2, 3],
                keys=[[1], [2], []],
                containedBoxes=[[1], [2], []],
                initialBoxes=[0],
            ),
            6,
        )

    def test_complex_cases(self):
        # Test case with multiple boxes, keys, and contained boxes
        self.assertEqual(
            self.solution.maxCandies(
                status=[1, 0, 0, 0],
                candies=[1, 2, 3, 4],
                keys=[[1], [2], [3], []],
                containedBoxes=[[1], [2], [3], []],
                initialBoxes=[0],
            ),
            10,
        )

        # Test case with unreachable boxes
        self.assertEqual(
            self.solution.maxCandies(
                status=[1, 0, 0],
                candies=[1, 2, 3],
                keys=[[], [], []],
                containedBoxes=[[], [], []],
                initialBoxes=[0],
            ),
            1,
        )

    def test_edge_cases(self):
        # Test case with no initial boxes
        self.assertEqual(
            self.solution.maxCandies(
                status=[1, 1, 1],
                candies=[1, 2, 3],
                keys=[[], [], []],
                containedBoxes=[[], [], []],
                initialBoxes=[],
            ),
            0,
        )

        # Test case with all boxes closed and no keys
        self.assertEqual(
            self.solution.maxCandies(
                status=[0, 0, 0],
                candies=[1, 2, 3],
                keys=[[], [], []],
                containedBoxes=[[], [], []],
                initialBoxes=[0, 1, 2],
            ),
            0,
        )


if __name__ == "__main__":
    unittest.main()
