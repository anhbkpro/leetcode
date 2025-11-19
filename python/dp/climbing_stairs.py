from abc import ABC, abstractmethod


class SolutionBase(ABC):
    @abstractmethod
    def climbStairs(self, n: int) -> int:
        pass


class SolutionDP(SolutionBase):
    def climbStairs(self, n: int) -> int:
        # Initialize the base cases for the number of ways to climb 0, 1, and 2 stairs.
        dp = [1, 1, 2]
        # Iterate over the remaining stairs and calculate the number of ways to climb each stair.
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]


class SolutionRecursionMemoization(SolutionBase):
    def climbStairs(self, n: int) -> int:
        # Initialize the memoization dictionary.
        self.memo = {}
        return self.calculate_ways(n)

    def calculate_ways(self, n: int) -> int:
        # Check if the number of ways to climb `n` stairs is already memoized.
        if n in self.memo:
            return self.memo[n]
        # Base cases for the number of ways to climb 0, 1, and 2 stairs.
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        # Calculate the number of ways to climb `n` stairs by summing the ways to climb `n-1` and `n-2` stairs.
        result = self.calculate_ways(n - 1) + self.calculate_ways(n - 2)
        # Memoize the result for future reference.
        self.memo[n] = result
        return result
