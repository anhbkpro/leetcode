class SolutionOnSpace:
    """
    Time complexity : O(N) time to perform N/2 swaps.
    Space complexity : O(N) to keep the recursion stack.
    """

    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)


class SolutionO1Space:
    """
    Time complexity : O(N) time to perform N/2 swaps.
    Space complexity : O(1), it's a constant space solution.
    """

    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
