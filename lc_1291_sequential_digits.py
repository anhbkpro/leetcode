from typing import List


class Solution:
    @staticmethod
    def sequentialDigits(low: int, high: int) -> List[int]:
        sample = "123456789"
        n = 10
        ans = []
        low_len = len(str(low))
        high_len = len(str(high))
        for length in range(low_len, high_len + 1):
            for i in range(n - length):
                num = int(sample[i:i + length])
                if low <= num <= high:
                    ans.append(num)
        return ans
