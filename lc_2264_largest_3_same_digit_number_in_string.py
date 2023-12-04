from collections import defaultdict


class Solution:
    @staticmethod
    def largestGoodInteger(num: str) -> str:
        left, right = 0, 0
        freq = defaultdict()
        current_max = -1
        ans = ""
        while right < len(num):
            if num[right] not in freq:
                freq[num[right]] = 0
            freq[num[right]] += 1
            while len(freq) > 1:
                freq[num[left]] -= 1
                if freq[num[left]] <= 0:
                    del freq[num[left]]
                left += 1
            if right - left == 2:
                if current_max <= int(num[left: right + 1]):
                    ans = num[left: right + 1]
                    current_max = int(num[left: right + 1])
            right += 1

        if current_max >= 0:
            return ans

        return ""
