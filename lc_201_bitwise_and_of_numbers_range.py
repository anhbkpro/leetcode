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
        shift = 0
        # find the common 1-bits
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift
