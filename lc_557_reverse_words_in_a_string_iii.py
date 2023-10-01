class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        strs = s.split(' ')
        rv = []
        for item in strs:
            rv.append(item[::-1])

        return ' '.join(rv)
