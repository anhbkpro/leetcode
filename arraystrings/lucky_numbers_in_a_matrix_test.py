from .lucky_numbers_in_a_matrix import Solution


# Returns the lucky number when it exists in the matrix
def test_lucky_number_exists_1():
    solution = Solution()
    matrix = [
        [3, 7, 8],
        [9, 11, 13],
        [15, 16, 17]
    ]
    assert solution.luckyNumbers(matrix) == [15]

def test_lucky_number_exists_2():
    solution = Solution()
    matrix = [[7,8],[1,2]]
    assert solution.luckyNumbers(matrix) == [7]
