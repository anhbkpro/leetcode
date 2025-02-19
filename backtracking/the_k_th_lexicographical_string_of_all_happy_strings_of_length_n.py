class Solution:
    def generateHappyStrings(self, n, curr_str, happy_strs):
        if len(curr_str) == n:
            happy_strs.append(curr_str)
            return

        for curr_char in ["a", "b", "c"]:
            if len(curr_str) > 0 and curr_char == curr_str[-1]:
                continue
            self.generateHappyStrings(n, curr_str + curr_char, happy_strs)

    def getHappyString(self, n: int, k: int) -> str:
        happy_strs = []
        self.generateHappyStrings(n, "", happy_strs)
        if len(happy_strs) < k:
            return ""

        happy_strs.sort()
        return happy_strs[k - 1]
