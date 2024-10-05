from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counter = Counter(s1)
        window_counter = Counter()

        for right in range(len(s2)):
            # Add the rightmost character to the window
            window_counter[s2[right]] += 1

            # If the window size is larger than s1, remove the leftmost character
            if right >= len(s1):
                left = right - len(s1)
                if window_counter[s2[left]] == 1:
                    del window_counter[s2[left]]
                else:
                    window_counter[s2[left]] -= 1

            # Check if the current window is a permutation of s1
            if window_counter == s1_counter:
                return True

        return False
