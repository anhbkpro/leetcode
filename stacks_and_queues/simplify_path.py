class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for d in path.split("/"):
            if not d or d == ".":
                continue
            if d == "..":
                if stack:
                    stack.pop()
                continue

            stack.append(d)

        return "/" + "/".join(stack)
