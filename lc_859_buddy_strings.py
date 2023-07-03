from collections import deque


# Below is my solution:

def buddyStrings(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    char_map = {}
    did_swap = False
    for c in s:
        char_map[c] = True

    if s == goal:
        if len(char_map) < len(s):
            return True
        return False

    first_diff = deque()
    for i in range(len(s)):
        if s[i] == goal[i]:
            continue

        if did_swap:
            return False

        if not first_diff:
            first_diff.append(i)
            continue
        else:
            did_swap = True
            item = first_diff.popleft()
            if goal[item] != s[i] or goal[i] != s[item]:
                return False

    if len(first_diff) > 0:
        return False

    return True


class Solution:
    pass
