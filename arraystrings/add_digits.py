class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        tem_str = str(num)
        temp_num = 10
        while temp_num >= 10:
            temp_num = 0
            for ch in tem_str:
                temp_num += int(ch)
            tem_str = str(temp_num)
        return temp_num
