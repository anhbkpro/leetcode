class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for c in s:
            if c == "(":
                low += 1
                high += 1

            elif c == ")":
                low -= 1
                high -= 1

            else:  # c == "*"
                low -= 1
                high += 1

            # Minimum balance cannot be negative.
            low = max(low, 0)

            # Even the maximum possible balance is negative.
            if high < 0:
                return False

        # There must be a way to have exactly 0 unmatched '('.
        return low == 0