class Solution:
    def maximum69Number(self, num: int) -> int:
        num_char_list = list(str(num))
        for i, c in enumerate(num_char_list):
            if c == "6":
                num_char_list[i] = "9"
                break
        return int("".join(num_char_list))


class Solution2:
    def maximum69Number(self, num: int) -> int:
        # Convert the input 'num' to the string 'num_string'.
        num_string = str(num)

        # Use the built-in function to replace the first '6' with '9'.
        # Return the integer converted from the modified 'num_string'.
        return int(num_string.replace("6", "9", 1))
