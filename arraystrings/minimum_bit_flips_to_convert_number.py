class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def to_binary(number):
            return bin(number)[2:]

        start_bin = str(to_binary(start))
        goal_bin = str(to_binary(goal))
        start_len = len(start_bin)
        goal_len = len(goal_bin)
        min_len = min(start_len, goal_len)
        ans = 0

        for s, g in zip(start_bin[-min_len:], goal_bin[-min_len:]):
            if s != g:
                ans += 1

        return ans + start_bin[:(start_len - min_len)].count("1") + goal_bin[:(goal_len - min_len)].count("1")
