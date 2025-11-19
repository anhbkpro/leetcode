class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min_adds_required = 0
        for c in s:
            if c == "(":
                min_adds_required += 1
            else:
                if min_adds_required > 0:
                    min_adds_required -= 1
                else:
                    open_brackets += 1
        return open_brackets + min_adds_required
