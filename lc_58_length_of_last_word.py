class Solution:
    @staticmethod
    def lengthOfLastWord(s: str) -> int:
        return len(s.split()[-1])
