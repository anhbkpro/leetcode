def shortestWay(source: str, target: str) -> int:
    # To check if to_check is subsequence of in_string
    def is_subsequence(to_check, in_string):
        # i is the index of to_check
        # j is the index of in_string
        i = j = 0
        while i < len(to_check) and j < len(in_string):
            if to_check[i] == in_string[j]:
                i += 1
            j += 1
        return i == len(to_check)

    # Set of all characters of source. Can use a boolean array too.
    source_set = set(source)
    # Check if all characters of target are present in source
    # If any character is not present, return -1
    for char in target:
        if char not in source_set:
            return -1

    # Concatenate source until target is a subsequence
    # of the concatenated string
    concatenated_source = source
    count = 1
    while not is_subsequence(target, concatenated_source):
        concatenated_source += source
        count += 1

    # Number of concatenations done
    return count


class Solution:
    pass
