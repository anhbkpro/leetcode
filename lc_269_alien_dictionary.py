from typing import List


def alienOrder(words: List[str]) -> str:
    # Step 0: create data structures + the in_degree of each unique letter to 0.
    adj_list = {c: set() for word in words for c in word}
    in_degree = {c: 0 for word in words for c in word}

    # Step 1: We need to populate adj_list and in_degree.
    # For each pair of adjacent words...
    for first_word, second_word in zip(words, words[1:]):
        # Check that second word isn't a prefix of first word.
        if len(first_word) > len(second_word) and first_word.startswith(second_word):
            return ""
        # Find the first non match and insert the corresponding relation.
        for c, d in zip(first_word, second_word):
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    in_degree[d] += 1
                break

    # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
    output = []
    queue = [c for c in in_degree if in_degree[c] == 0]
    while queue:
        c = queue.pop()
        output.append(c)
        for d in adj_list[c]:
            in_degree[d] -= 1
            if in_degree[d] == 0:
                queue.append(d)

    # If not all letters are in output, that means there was a cycle and so
    # no valid ordering. Return "" as per the problem description.
    if len(output) < len(in_degree):
        return ""
    return "".join(output)


class Solution:
    pass
