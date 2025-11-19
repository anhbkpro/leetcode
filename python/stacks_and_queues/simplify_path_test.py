import unittest
from .simplify_path import Solution


class TestSimplifyPath(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        path = "/home/"
        expected = "/home"
        self.assertEqual(self.solution.simplifyPath(path), expected)

    def test_example_2(self):
        path = "/../"
        expected = "/"
        self.assertEqual(self.solution.simplifyPath(path), expected)

    def test_example_3(self):
        path = "/home//foo/"
        expected = "/home/foo"
        self.assertEqual(self.solution.simplifyPath(path), expected)

    def test_example_4(self):
        path = "/a/./b/../../c/"
        expected = "/c"
        self.assertEqual(self.solution.simplifyPath(path), expected)

    def test_empty_path(self):
        path = ""
        expected = ""
        self.assertEqual(self.solution.simplifyPath(path), expected)

    def test_root_path(self):
        path = "/"
        expected = "/"
        self.assertEqual(self.solution.simplifyPath(path), expected)

    def test_multiple_slashes(self):
        path = "/home///test////file"
        expected = "/home/test/file"
        self.assertEqual(self.solution.simplifyPath(path), expected)

    def test_current_directory(self):
        path = "/home/./test/./file/."
        expected = "/home/test/file"
        self.assertEqual(self.solution.simplifyPath(path), expected)

    def test_parent_directory(self):
        path = "/home/test/../file"
        expected = "/home/file"
        self.assertEqual(self.solution.simplifyPath(path), expected)

    def test_multiple_parent_directory(self):
        path = "/home/test/../../file"
        expected = "/file"
        self.assertEqual(self.solution.simplifyPath(path), expected)

    def test_beyond_root_directory(self):
        path = "/home/../../.."
        expected = "/"
        self.assertEqual(self.solution.simplifyPath(path), expected)

    def test_complex_path(self):
        path = "/home/user/./documents/../downloads/./music/.."
        expected = "/home/user/downloads"
        self.assertEqual(self.solution.simplifyPath(path), expected)


if __name__ == "__main__":
    unittest.main()
