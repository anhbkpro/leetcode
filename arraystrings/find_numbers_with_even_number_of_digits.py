from typing import List


class ConvertToString:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)


class ExtractDigits:
    def has_even_digits(self, num: int) -> bool:
        cnt = 0
        while num > 0:
            cnt += 1
            num //= 10

        return False if cnt % 2 else True

    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if self.has_even_digits(num):
                ans += 1
        return ans
