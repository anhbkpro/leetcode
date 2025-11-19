class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        rev_s = s[::-1]
        temp = s + "#" + rev_s

        # Compute the KMP failure function
        lps = [0] * len(temp)
        length = 0
        i = 1

        while i < len(temp):
            if temp[i] == temp[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # The length of the longest proper prefix which is also a suffix
        longest_prefix_suffix = lps[-1]

        # Add the remaining characters in reverse order
        return rev_s[:-longest_prefix_suffix] + s
