import unittest

from two_pointers.compare_version_numbers import Solution


class TestCompareVersionNumbers(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.compareVersion("1.2", "1.10"), -1)

    def test_example2(self):
        self.assertEqual(self.sol.compareVersion("1.01", "1.001"), 0)

    def test_example3(self):
        self.assertEqual(self.sol.compareVersion("1.0", "1.0.0.0"), 0)

    def test_version1_greater(self):
        self.assertEqual(self.sol.compareVersion("2.0", "1.9.9"), 1)

    def test_version2_greater(self):
        self.assertEqual(self.sol.compareVersion("1.0.1", "1.1"), -1)

    def test_trailing_zeros(self):
        self.assertEqual(self.sol.compareVersion("1.0.0", "1"), 0)

    def test_leading_zeros(self):
        self.assertEqual(self.sol.compareVersion("01.0.0", "1"), 0)

    def test_long_versions(self):
        self.assertEqual(self.sol.compareVersion("1.0.0.0.0.0.1", "1.0.0.0.0.0.0"), 1)

    def test_all_zeros(self):
        self.assertEqual(self.sol.compareVersion("0.0.0", "0"), 0)


if __name__ == "__main__":
    unittest.main()
