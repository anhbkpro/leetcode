from typing import List


class Solution:
    @staticmethod
    def plus_one(digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            if digits[i] + carry >= 10:
                digits[i] = digits[i] + carry - 10
                carry = 1
            else:
                digits[i] = digits[i] + carry
                carry = 0
        if carry == 1:
            return [1] + digits

        return digits
