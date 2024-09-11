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

    def minBitFlipsByShiftBit(self, start: int, goal: int) -> int:
        count = 0
        while start > 0 or goal > 0:
            # Increment count if the current bits differ
            if (start & 1) != (goal & 1):
                count += 1
            # Shift both numbers to the right to check the next bits
            start >>= 1
            goal >>= 1
        return count
