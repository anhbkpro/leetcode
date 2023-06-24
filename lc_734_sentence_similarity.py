from collections import defaultdict
from typing import List


def areSentencesSimilar(sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
    if len(sentence1) != len(sentence2):
        return False

    similar_map = defaultdict(list)
    for sp in range(len(similarPairs)):
        similar_map[similarPairs[sp][0]].append(similarPairs[sp][1])
        similar_map[similarPairs[sp][1]].append(similarPairs[sp][0])

    for i in range(len(sentence1)):
        if sentence1[i] == sentence2[i]:
            continue
        elif sentence1[i] != sentence2[i] and sentence2[i] not in similar_map[sentence1[i]]:
            return False

    return True


class Solution:
    pass
