class Solution:
    @staticmethod
    def countSubstrings(s: str) -> int:
        def is_palindrome(s: str, lo: int, hi: int) -> bool:
            while lo < hi:
                if s[lo] != s[hi]:
                    return False

                lo += 1
                hi -= 1

            return True

        ans = 0
        for lo in range(len(s)):
            for hi in range(lo, len(s)):
                ans += is_palindrome(s, lo, hi)

        return ans
