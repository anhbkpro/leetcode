from bisect import bisect_left
from typing import List


def successful_pairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    # Sort the potions array in increasing order.
    potions.sort()
    answer = []

    m = len(potions)
    max_potion = potions[m - 1]

    for spell in spells:
        # Minimum value of potion whose product with current spell
        # will be at least success or more.
        min_potion = (success + spell - 1) // spell
        # Check if we don't have any potion which can be used.
        if min_potion > max_potion:
            answer.append(0)
            continue
        # We can use the found potion, and all potion in its right
        # (as the right potions are greater than the found potion).
        index = bisect_left(potions, min_potion)
        answer.append(m - index)

    return answer


class Solution:
    pass
