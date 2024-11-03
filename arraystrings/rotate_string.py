class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        can_rotate = False
        for i in range(len(s)):
            temp_s = s[i:] + s[:i]
            if temp_s == goal:
                can_rotate = True
                break

        return can_rotate
