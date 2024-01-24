from typing import List


class Solution:
    @staticmethod
    def maxLength(arr: List[str]) -> int:
        # Initialize results with an empty string
        # from which to build all future results
        results = [""]
        best = 0
        for word in arr:
            # We only want to iterate through results
            # that existed prior to this loop
            for i in range(len(results)):
                # Form a new result combination and
                # use a set to check for duplicate characters
                new_res = results[i] + word  # `results` is built up from previous distinct `word`s
                if len(new_res) != len(set(new_res)):  # make sure no duplicate chars in feasible results
                    continue

                # Add valid options to results and
                # keep track of the longest so far
                results.append(new_res)
                # print(results)
                best = max(best, len(new_res))  # best till now (keep track of the longest valid result)
        return best
