from typing import List


class SolutionOptimizedBruteForce:
    """
    Time Limit Exceeded
    Time: O(N^3)
    Space: O(N)
    """

    def tupleSameProduct(self, nums: List[int]) -> int:
        nums_length = len(nums)
        nums.sort()

        total_number_of_tuples = 0

        # Iterate over all possible values for 'a'
        for a_index in range(nums_length):
            # Iterate over all possible values for 'b', starting from the end
            # of the list
            for b_index in range(nums_length - 1, a_index, -1):
                product = nums[a_index] * nums[b_index]

                # Use a set to store possible values of 'd'
                possible_d_values = set()

                # Iterate over all possible values for 'c' between 'a' and 'b'
                for c_index in range(a_index + 1, b_index):
                    # Check if the product is divisible by nums[c_index]
                    if product % nums[c_index] == 0:
                        d_value = product // nums[c_index]

                        # If 'd_value' is in the set, increment the tuple count
                        # by 8
                        if d_value in possible_d_values:
                            total_number_of_tuples += 8

                        # Add nums[c_index] to the set for future checks
                        possible_d_values.add(nums[c_index])

        return total_number_of_tuples


class SolutionCountProductFrequency:
    """
    Time: O(N^2logN)
    Space: O(N^2)
    """

    def tupleSameProduct(self, nums):
        nums_length = len(nums)

        pair_products = []

        total_number_of_tuples = 0

        # Iterate over nums to calculate all pairwise products
        for first_index in range(nums_length):
            for second_index in range(first_index + 1, nums_length):
                pair_products.append(nums[first_index] * nums[second_index])

        pair_products.sort()

        last_product_seen = -1
        same_product_count = 0

        # Iterate over pair_products to count how many times each product occurs
        for product_index in range(len(pair_products)):
            if pair_products[product_index] == last_product_seen:
                # Increment the count of same products
                same_product_count += 1
            else:
                # Calculate how many pairs had the previous product value
                pairs_of_equal_product = (
                    (same_product_count - 1) * same_product_count // 2
                )

                total_number_of_tuples += 8 * pairs_of_equal_product

                # Update last_product_seen and reset same_product_count
                last_product_seen = pair_products[product_index]
                same_product_count = 1

        # Handle the last group of products (since the loop ends without adding
        # it)
        pairs_of_equal_product = (same_product_count - 1) * same_product_count // 2
        total_number_of_tuples += 8 * pairs_of_equal_product

        return total_number_of_tuples


class SolutionProductFrequencyHashMap:
    """Find the number of tuples (i,j,k,l) such that nums[i] * nums[j] == nums[k] * nums[l].

    Time Complexity: O(N^2) where N is the length of nums
    Space Complexity: O(N^2) to store the product frequencies

    Example:
        >>> solution = SolutionProductFrequencyHashMap()
        >>> solution.tupleSameProduct([2,3,4,6])
        8
        >>> solution.tupleSameProduct([1,2,4,5,10])
        16
    """

    def __init__(self):
        from collections import defaultdict

        self.defaultdict = defaultdict

    def _calculate_tuples_for_frequency(self, frequency: int) -> int:
        """Calculate number of valid tuples for a given product frequency.

        For each pair of pairs with the same product, we can form 8 different
        tuples by arranging the numbers in different orders.

        Args:
            frequency: Number of pairs that produce the same product

        Returns:
            Number of valid tuples that can be formed
        """
        # Number of ways to choose 2 pairs from frequency pairs
        pairs_of_equal_product = (frequency - 1) * frequency // 2
        # Each pair can be arranged in 8 different ways
        return 8 * pairs_of_equal_product

    def tupleSameProduct(self, nums: List[int]) -> int:
        """Find number of tuples with equal products.

        Args:
            nums: List of integers to find tuples from

        Returns:
            Number of valid tuples (i,j,k,l) where nums[i] * nums[j] == nums[k] * nums[l]
            and i, j, k, and l are different indices
        """
        if len(nums) < 4:
            return 0

        # Use defaultdict to automatically initialize frequencies to 0
        product_freq = self.defaultdict(int)

        # Calculate frequencies of all possible products
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_freq[product] += 1

        # Sum up the number of tuples for each product frequency
        return sum(
            self._calculate_tuples_for_frequency(freq) for freq in product_freq.values()
        )
