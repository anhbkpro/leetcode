class Solution:
    def numberToWords(self, num: int) -> str:
        # Handle the special case where the number is zero
        if num == 0:
            return "Zero"

        # Arrays to store words for single digits, tens, and thousands
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        # StringBuilder to accumulate the result
        result = ""
        group_index = 0

        # Process the number in chunks of 1000
        while num > 0:
            # Process the last three digits, 1234567 -> 567
            if num % 1000 != 0:
                group_result = ""
                part = num % 1000

                # Handle hundreds
                if part >= 100:
                    group_result += ones[part // 100] + " Hundred " # 567 -> Five Hundred
                    part %= 100 # 567 -> 67

                # Handle tens and units
                if part >= 20:
                    group_result += tens[part // 10] + " " # 67 -> Sixty
                    part %= 10 # 67 -> 7

                # Handle units
                if part > 0:
                    group_result += ones[part] + " " # 7 -> Seven

                # 1234 [567], group_index = 0 -> "Five Hundred Sixty Seven"
                # 1 [234] 567, group_index = 1 -> "Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
                # [1] 234567, group_index = 2 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
                # Append the scale (thousand, million, billion) for the current group
                group_result += thousands[group_index] + " "
                # Insert the group result at the beginning of the final result
                result = group_result + result
            # Move to the next chunk of 1000
            num //= 1000 # 1234567 -> 1234
            group_index += 1

        return result.strip()
