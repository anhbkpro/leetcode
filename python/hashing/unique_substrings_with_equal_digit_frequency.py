class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        n = len(s)
        valid_substrings = set()

        for start in range(n):
            digit_frequency = [0] * 10
            for end in range(start, n):
                digit_frequency[ord(s[end]) - ord("0")] += 1
                common_frequency = 0
                is_valid = True

                for count in digit_frequency:
                    if count == 0:
                        continue
                    if common_frequency == 0:
                        common_frequency = count
                    if common_frequency != count:
                        is_valid = False
                        break
                if is_valid:
                    substring = s[start : end + 1]
                    valid_substrings.add(substring)
        return len(valid_substrings)
