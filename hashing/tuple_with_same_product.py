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
    """
    Time: O(N^2)
    Space: O(N^2)
    """

    def tupleSameProduct(self, nums):
        nums_length = len(nums)

        # Initialize a dictionary to store the frequency of each product of pairs
        pair_products_frequency = {}

        total_number_of_tuples = 0

        # Iterate through each pair of numbers in `nums`
        for first_index in range(nums_length):
            for second_index in range(first_index + 1, nums_length):
                # Increment the frequency of the product of the current pair
                product_value = nums[first_index] * nums[second_index]
                if product_value in pair_products_frequency:
                    pair_products_frequency[product_value] += 1
                else:
                    pair_products_frequency[product_value] = 1

        # Iterate through each product value and its frequency in the dictionary
        for product_frequency in pair_products_frequency.values():
            # Calculate the number of ways to choose two pairs with the same product
            pairs_of_equal_product = (product_frequency - 1) * product_frequency // 2

            # Add the number of tuples for this product to the total (each pair
            # can form 8 tuples)
            total_number_of_tuples += 8 * pairs_of_equal_product

        return total_number_of_tuples
