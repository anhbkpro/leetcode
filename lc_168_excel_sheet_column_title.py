class Solution(object):
    @staticmethod
    def convertToTitle(column_number):
        out = ""
        while column_number > 0:
            out = chr(ord('A') + (column_number - 1) % 26) + out
            column_number = (column_number - 1) // 26
        return out
