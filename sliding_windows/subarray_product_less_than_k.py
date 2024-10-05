from typing import List


class Solution:
    @staticmethod
    def num_subarray_product_less_than_k(nums: List[int], k: int) -> int:
        # Handle edge cases where k is 0 or 1 (no sub-arrays possible)
        if k <= 1:
            return 0

        total_count = 0
        product = 1

        # Use two pointers to maintain a sliding window
        left = 0
        for right, num in enumerate(nums):
            # Expand the window by including the element at the right pointer
            product *= num

            # Shrink the window from the left while the product is greater than or equal to k
            while product >= k:
                product //= nums[
                    left
                ]  # Remove the element at the left pointer from the product
                left += 1

            # Update the total count by adding the number of valid sub-arrays with the current window size
            total_count += (
                right - left + 1
            )  # right - left + 1 represents the current window size

        return total_count
