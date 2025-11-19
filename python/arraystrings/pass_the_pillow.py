class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        mod = time % (n - 1)
        round = time // (n - 1)
        if round % 2 == 0:
            return mod + 1
        return n - mod
