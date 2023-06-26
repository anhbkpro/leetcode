def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for c in s:
        if c in '({[':
            stack.append(c)
        else:
            if len(stack) == 0 or stack.pop() != mapping[c]:
                return False

    return not stack


class Solution:
    pass
