def shortestWay(source: str, target: str) -> int:
    # Set of all characters of source. Can use boolean array too.
    source_chars = set(source)

    # Check if all characters of target are present in source
    # If any character is not present, return -1
    for char in target:
        if char not in source_chars:
            return -1

    # Length of source to loop back to start of source using mod
    m = len(source)

    # Pointer for source
    source_iterator = 0

    # Number of times source is traversed. It will be incremented when
    # while finding occurrence of a character in target, source_iterator
    # reaches the start of source again.
    count = 0

    # Find all characters of target in source
    for char in target:
        # If while finding, iterator reaches start of source again,
        # increment count
        if source_iterator == 0:
            count += 1

        #  source = "abc"
        #  target = "abcbc"

        # Find the first occurrence of char in source
        while source[source_iterator % m] != char:
            source_iterator += 1

            # If while finding, iterator reaches start of source again,
            # increment count
            if source_iterator % m == 0:
                count += 1

        # Loop will break when char is found in source. Thus, increment.
        # Don't increment count until it is not clear that target has
        # remaining characters.
        source_iterator = (source_iterator + 1) % m

    return count




class Solution:
    pass
