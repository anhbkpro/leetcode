from collections import Counter


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cnt = [k for k, v in Counter(num).items() if v >= 3]
        ans = ""
        max_num = -1
        for i in cnt:
            if (3 * i in num) and int(i) > max_num:
                max_num = int(i)
        if max_num == -1:
            return ""

        return 3 * f"{max_num}"
