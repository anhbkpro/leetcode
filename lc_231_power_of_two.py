class Solution:
    def is_power_of_two(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 2 == 1:
            return False
        return self.is_power_of_two(n // 2)
