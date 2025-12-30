import unittest

from .top_k_element import topKFrequent


class TestTopKFrequent(unittest.TestCase):
    def test_topKFrequent(self):
        self.assertEqual(topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
        self.assertEqual(topKFrequent([1], 1), [1])
        self.assertEqual(topKFrequent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [10, 9, 8])
        self.assertEqual(topKFrequent([4, 4, 4, 4, 5, 5, 5, 6, 6, 7], 2), [4, 5])
        self.assertEqual(
            topKFrequent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], 1), [10]
        )


if __name__ == "__main__":
    unittest.main()
