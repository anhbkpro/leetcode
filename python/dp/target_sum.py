from abc import ABC, abstractmethod
from typing import List


class SolutionBase(ABC):
    @abstractmethod
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        pass


class SolutionBF(SolutionBase):
    def __init__(self):
        # Tracks the total number of ways to reach the target
        self.total_ways = 0

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Reset total_ways for each new calculation
        self.total_ways = 0
        self.calculate_ways(nums, 0, 0, target)
        return self.total_ways

    def calculate_ways(
        self, nums: List[int], current_index: int, current_sum: int, target: int
    ):
        if current_index == len(nums):
            # Check if the current sum matches the target
            if current_sum == target:
                self.total_ways += 1
        else:

            # Include the current number with a positive sign
            self.calculate_ways(
                nums,
                current_index + 1,
                current_sum + nums[current_index],
                target,
            )

            # Include the current number with a negative sign
            self.calculate_ways(
                nums,
                current_index + 1,
                current_sum - nums[current_index],
                target,
            )


class SolutionMemoization(SolutionBase):
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Initialize the memoization dictionary
        self.memo = {}
        return self.calculate_ways(nums, 0, 0, target)

    def calculate_ways(
        self, nums: List[int], current_index: int, current_sum: int, target: int
    ):
        # Check if the current index and sum are already memoized
        if (current_index, current_sum) in self.memo:
            return self.memo[(current_index, current_sum)]

        # Base case: if we reach the end of the array
        if current_index == len(nums):
            # Check if the current sum matches the target
            if current_sum == target:
                return 1
            return 0

        # Include the current number with a positive sign
        positive_ways = self.calculate_ways(
            nums,
            current_index + 1,
            current_sum + nums[current_index],
            target,
        )

        # Include the current number with a negative sign
        negative_ways = self.calculate_ways(
            nums,
            current_index + 1,
            current_sum - nums[current_index],
            target,
        )

        # Store the result in the memoization dictionary
        self.memo[(current_index, current_sum)] = positive_ways + negative_ways

        return self.memo[(current_index, current_sum)]
