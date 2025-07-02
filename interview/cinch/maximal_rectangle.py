def maximal_rectangle(matrix):
    """
    Returns the area of the largest rectangle containing only '1's.

    Args:
        matrix: List of lists containing '0' and '1' characters

    Returns:
        int: Maximum rectangular area of '1's
    """
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for i in range(rows):
        # Build histogram heights for current row
        for j in range(cols):
            if matrix[i][j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0

        # Find largest rectangle in current histogram
        area = largest_rectangle_in_histogram(heights)
        max_area = max(max_area, area)

    return max_area


def largest_rectangle_in_histogram(heights):
    """
    Finds the largest rectangular area in a histogram.

    Args:
        heights: List of integers representing histogram bar heights

    Returns:
        int: Maximum rectangular area
    """
    if not heights:
        return 0

    stack = []  # Stack to store indices
    max_area = 0

    # Process all bars including a sentinel 0 at the end
    for i in range(len(heights) + 1):
        # Use 0 as sentinel value for the last iteration
        h = 0 if i == len(heights) else heights[i]

        # While stack is not empty and current height is less than stack top
        while stack and h < heights[stack[-1]]:
            # Pop the top element
            height = heights[stack.pop()]

            # Calculate width
            width = i if not stack else i - stack[-1] - 1

            # Calculate area and update max
            area = height * width
            max_area = max(max_area, area)

        # Push current index to stack
        stack.append(i)

    return max_area


def run_tests():
    """Execute test cases against maximal_rectangle function."""
    test_cases = [
        # empty matrix
        ([], 0),
        # single '0'
        ([['0']], 0),
        # single '1'
        ([['1']], 1),
        # example from prompt
        ([
            ['1','0','1','0','0'],
            ['1','0','1','1','1'],
            ['1','1','1','1','1'],
            ['1','0','0','1','0'],
        ], 6),
        # full block of '1's
        ([
            ['1','1','1','1'],
            ['1','1','1','1'],
            ['1','1','1','1'],
        ], 12),
        # single row with a gap; max consecutive '1's = 2
        ([['1','1','0','1']], 2),
        # 3×4 matrix with one zero in top right; largest 3×3 block = 9
        ([
            ['1','1','1','0'],
            ['1','1','1','1'],
            ['1','1','1','1'],
        ], 9),
    ]

    for i, (matrix, expected) in enumerate(test_cases, 1):
        result = maximal_rectangle(matrix)
        if result != expected:
            print(f"*** Test {i} FAILED: got {result}, want {expected}")
            return False
        print(f"Test {i} passed: {result}")

    print(f"All {len(test_cases)} tests passed!")
    return True


if __name__ == "__main__":
    run_tests()
