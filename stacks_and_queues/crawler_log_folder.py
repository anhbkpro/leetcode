from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        position = []
        for log in logs:
            if log == './':
                continue
            if log == '../':
                if position:
                    position.pop()
                else:
                    continue
            else:
                position.append(log)
        return len(position)
