from typing import List


class Solution:
    @staticmethod
    def plus_one(digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            current_sum = digits[i] + carry
            digits[i] = current_sum % 10
            carry = current_sum // 10

        if carry == 1:
            return [1] + digits

        return digits
