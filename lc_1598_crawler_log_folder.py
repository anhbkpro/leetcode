from typing import List


class Solution:
    @staticmethod
    def minOperations(logs: List[str]) -> int:
        stack = []
        for i in range(len(logs)):
            if logs[i] == "./" or (logs[i] == "../" and len(stack) == 0):
                continue
            elif logs[i] == "../" and len(stack) > 0:
                stack.pop()
            else:
                stack.append(logs[i])

        return len(stack)
