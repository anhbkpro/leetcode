class Solution:
    @staticmethod
    def minOperations(s: str) -> int:
        ans = 0
        ans = min(Solution.helper(s, False), Solution.helper(s, True))
        return ans

    @staticmethod
    def helper(s: str, flip: bool) -> int:
        ans = 0
        if flip:
            first = "1" if s[0] == "0" else "0"
        else:
            first = s[0]

        second = "0" if first == "1" else "1"
        for i in range(0, len(s)):
            if i % 2 == 0:
                if s[i] != first:
                    ans += 1
            else:
                if s[i] != second:
                    ans += 1

        return ans
