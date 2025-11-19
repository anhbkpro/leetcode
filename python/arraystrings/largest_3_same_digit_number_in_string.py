from collections import Counter


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cnt = [k for k, v in Counter(num).items() if v >= 3]
        return max((3 * i for i in cnt if 3 * i in num), default="")
