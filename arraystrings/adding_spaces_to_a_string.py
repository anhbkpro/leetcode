from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # List to store characters (more efficient than string concatenation)
        ans = []
        space_index = 0
        for i, c in enumerate(s):
            if space_index < len(spaces) and i == spaces[space_index]:
                # Insert space at the correct position
                ans.append(" ")
                space_index += 1

            # Append the current character
            ans.append(c)

        # Join all characters into final string
        return "".join(ans)
