from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder_stack = []
        for current_operation in logs:
            if current_operation == "../":
                if folder_stack:
                    folder_stack.pop()
            elif current_operation != "./":
                folder_stack.append(current_operation)

        return len(folder_stack)
