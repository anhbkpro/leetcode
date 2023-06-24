from collections import defaultdict
from typing import List


def areSentencesSimilar(sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
    if len(sentence1) != len(sentence2):
        return False

    similar_map = defaultdict(set)
    for word1, word2 in similarPairs:
        similar_map[word1].add(word2)
        similar_map[word2].add(word1)

    for i in range(len(sentence1)):
        if sentence1[i] == sentence2[i] or sentence2[i] in similar_map[sentence1[i]]:
            continue
        return False

    return True


class Solution:
    pass
