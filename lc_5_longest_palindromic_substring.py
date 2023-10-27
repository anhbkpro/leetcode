class Solution:
    @staticmethod
    def longest_palindrome(s: str) -> str:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        :param s: string
        :return: longest palindrome substring
        """
        # Initialize n = len(s) and a boolean table dp with size n * n, and all values to False.
        n = len(s)
        # dp[i][j] is a boolean representing if the substring with inclusive bounds i, j is a palindrome
        # dp[i][j] = True if s[i:j+1] is palindrome
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        # diff = 0
        # initialize dp[i][i] = true for the substrings of length 1
        for i in range(n):
            dp[i][i] = True

        # diff = 1
        # and then dp[i][i + 1] = (s[i] == s[i + 1]) for the substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        # diff >= 2 -> n
        # starting with pairs that have a difference of 2 (representing substrings of length 3),
        # then pairs with a difference of 3, then 4, and so on
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    # Because we are starting with the shortest substrings and iterating toward the longest
                    # substrings, every time we find a new palindrome, it must be the longest one we have seen so
                    # far. We can use this fact to keep track of the answer on the fly.
                    ans = [i, j]

        i, j = ans
        return s[i:j + 1]
