from .find_the_number_of_ways_to_place_people_i import Solution


def test_number_of_pairs_example1():
    """Test Example 1: points = [[1,1],[2,2],[3,3]] -> Output: 0"""
    solution = Solution()
    points = [[1, 1], [2, 2], [3, 3]]
    expected = 0
    actual = solution.numberOfPairs(points)
    assert actual == expected, f"Expected {expected}, but got {actual}"


def test_number_of_pairs_example2():
    """Test Example 2: points = [[6,2],[4,4],[2,6]] -> Output: 2"""
    solution = Solution()
    points = [[6, 2], [4, 4], [2, 6]]
    expected = 2
    actual = solution.numberOfPairs(points)
    assert actual == expected, f"Expected {expected}, but got {actual}"


def test_number_of_pairs_example3():
    """Test Example 3: points = [[3,1],[1,3],[1,1]] -> Output: 2"""
    solution = Solution()
    points = [[3, 1], [1, 3], [1, 1]]
    expected = 2
    actual = solution.numberOfPairs(points)
    assert actual == expected, f"Expected {expected}, but got {actual}"


def test_number_of_pairs_edge_cases():
    """Test edge cases"""
    solution = Solution()

    # Test with single point
    points = [[1, 1]]
    expected = 0
    actual = solution.numberOfPairs(points)
    assert actual == expected, f"Expected {expected}, but got {actual}"

    # Test with two points that can form a valid pair
    points = [[1, 3], [2, 1]]  # pointA[0] <= pointB[0] and pointA[1] >= pointB[1]
    expected = 1
    actual = solution.numberOfPairs(points)
    assert actual == expected, f"Expected {expected}, but got {actual}"

    # Test with two points that cannot form a valid pair
    points = [[1, 1], [2, 2]]  # pointA[0] <= pointB[0] but pointA[1] < pointB[1]
    expected = 0
    actual = solution.numberOfPairs(points)
    assert actual == expected, f"Expected {expected}, but got {actual}"


def test_number_of_pairs_empty_input():
    """Test with empty input"""
    solution = Solution()
    points = []
    expected = 0
    actual = solution.numberOfPairs(points)
    assert actual == expected, f"Expected {expected}, but got {actual}"


if __name__ == "__main__":
    # Run all tests
    test_number_of_pairs_example1()
    test_number_of_pairs_example2()
    test_number_of_pairs_example3()
    test_number_of_pairs_edge_cases()
    test_number_of_pairs_empty_input()
    print("All tests passed!")
