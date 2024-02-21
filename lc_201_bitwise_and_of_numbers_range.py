class Solution:
    @staticmethod
    def range_bitwise_and(left: int, right: int) -> int:
        """
        Time complexity: O(1)
        Space complexity: O(1)
        :type left: int
        :type right: int
        :param left:
        :param right:
        :return:
        """
        while left < right:
            # turn off rightmost 1-bit
            right &= right - 1
        return left & right
