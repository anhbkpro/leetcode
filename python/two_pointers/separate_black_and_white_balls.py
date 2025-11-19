class Solution:
    def minimumSteps(self, s: str) -> int:
        total_swaps = 0
        right = len(s) - 1
        white_ball_count = 0
        while right >= 0:
            if s[right] == "0":
                white_ball_count += 1
            else:
                total_swaps += white_ball_count
            right -= 1
        return total_swaps
