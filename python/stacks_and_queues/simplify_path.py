class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return path

        stack = []
        for p in path.split("/"):
            if p == "..":
                stack = stack[:-1]
            elif not p or p == ".":
                continue
            else:
                stack.append(p)

        return "/" + "/".join(stack)
