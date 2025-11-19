from .keep_multiplying_found_values_by_two import Solution


class TestFindFinalValue:
    def test_basic_case_with_multiplications(self):
        """Test case where multiple values are found and multiplied by 2"""
        solution = Solution()
        nums = [8, 1, 6, 4, 2]
        original = 1
        assert solution.findFinalValue(nums, original) == 16

    def test_no_matching_values(self):
        """Test case where original value is not found in nums"""
        solution = Solution()
        nums = [1, 2, 3, 4, 5]
        original = 10
        assert solution.findFinalValue(nums, original) == 10

    def test_single_match(self):
        """Test case where only one match is found"""
        solution = Solution()
        nums = [5, 10, 2]
        original = 5
        assert solution.findFinalValue(nums, original) == 20

    def test_empty_list(self):
        """Test case with empty list"""
        solution = Solution()
        nums = []
        original = 7
        assert solution.findFinalValue(nums, original) == 7

    def test_single_element_match(self):
        """Test case with single element that matches"""
        solution = Solution()
        nums = [3]
        original = 3
        assert solution.findFinalValue(nums, original) == 6

    def test_consecutive_multiplications(self):
        """Test case where consecutive doublings occur"""
        solution = Solution()
        nums = [1, 2, 4]
        original = 1
        assert solution.findFinalValue(nums, original) == 8

    def test_with_duplicates(self):
        """Test case with duplicate values in nums"""
        solution = Solution()
        nums = [2, 4, 8, 2]
        original = 2
        assert solution.findFinalValue(nums, original) == 16

    def test_large_numbers(self):
        """Test case with large numbers"""
        solution = Solution()
        nums = [1024, 512, 256]
        original = 256
        assert solution.findFinalValue(nums, original) == 2048
