from .unique_substrings_with_equal_digit_frequency import Solution


def test_example_1():
    """Test the first example case: s = "1212" """
    solution = Solution()
    result = solution.equalDigitFrequency("1212")
    assert result == 5


def test_example_2():
    """Test the second example case: s = "12321" """
    solution = Solution()
    result = solution.equalDigitFrequency("12321")
    assert result == 9


def test_single_digit():
    """Test with a single digit string"""
    solution = Solution()
    result = solution.equalDigitFrequency("1")
    assert result == 1


def test_all_same_digits():
    """Test with string containing all same digits"""
    solution = Solution()
    result = solution.equalDigitFrequency("333")
    assert result == 3


def test_no_equal_frequency():
    """Test with string having no substrings with equal frequency except single digits"""
    solution = Solution()
    result = solution.equalDigitFrequency("112")
    assert result == 4


def test_multiple_equal_frequency():
    """Test with string having multiple equal frequency substrings"""
    solution = Solution()
    result = solution.equalDigitFrequency("11223344")
    expected = set(
        [
            "1",
            "11",
            "1122",
            "112233",
            "11223344",
            "12",
            "2",
            "22",
            "2233",
            "223344",
            "23",
            "3",
            "33",
            "3344",
            "34",
            "4",
            "44",
        ]
    )
    assert result == len(expected)


def test_max_length():
    """Test with a string of maximum allowed length (1000)"""
    s = "12" * 500  # 1000 characters
    solution = Solution()
    result = solution.equalDigitFrequency(s)
    assert result > 0
