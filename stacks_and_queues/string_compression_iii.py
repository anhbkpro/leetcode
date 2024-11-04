class Solution:
    def compressedString(self, word: str) -> str:
        stack = []
        for c in word:
            if stack and stack[-1][-1] == c:
                if stack[-1][0] == 9:
                    stack.append([1, c])
                else:
                    stack[-1] = [stack[-1][0] + 1, c]
            else:
                stack.append([1, c])
        return "".join([f"{e[0]}{e[1]}" for e in stack])
