class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ords = [str(ord(ch) - ord("a") + 1) for ch in s]
        temp_str = "".join(ords)
        temp_num = 0
        for i in range(k):
            temp_num = 0
            for num in temp_str:
                temp_num += int(num)
            temp_str = str(temp_num)

        return temp_num
