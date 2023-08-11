from typing import List


class Solution:
    @staticmethod
    def change(amount: int, coins: List[int]) -> int:
        def numberOfWays(i: int, remain_amount: int) -> int:
            if remain_amount == 0:
                return 1

            if i == len(coins):
                return 0

            if memo[i][remain_amount] != -1:
                return memo[i][remain_amount]

            if coins[i] > remain_amount:
                memo[i][remain_amount] = numberOfWays(i + 1, remain_amount)
            else:
                memo[i][remain_amount] = numberOfWays(i, remain_amount - coins[i]) + numberOfWays(i + 1, remain_amount)

            return memo[i][remain_amount]

        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        return numberOfWays(0, amount)

    # Refactored `if coins[i] > amount condition` to `remain < 0`, which is more intuitive.
    @staticmethod
    def refactored_change(amount: int, coins: List[int]) -> int:
        def numberOfWays(i: int, remain: int) -> int:
            if remain == 0:
                return 1

            if i == n or remain < 0:
                return 0

            if memo[i][remain] != -1:
                return memo[i][remain]

            memo[i][remain] = numberOfWays(i, remain - coins[i]) + numberOfWays(i + 1, remain)
            return memo[i][remain]

        n = len(coins)
        memo = [[-1] * (amount + 1) for _ in range(n)]
        return numberOfWays(0, amount)
