class Solution:
    @staticmethod
    def maximum_odd_binary_number(s: str) -> str:
        n = len(s)
        ones = s.count('1')
        zeros = n - ones
        return "1" * (ones - 1) + "0" * zeros + "1"
