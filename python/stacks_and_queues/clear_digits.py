class SolutionStackLike:
    def clearDigits(self, s: str) -> str:
        # Use a list to store characters for efficient modification
        answer = []

        # Iterate over each character in the input string
        for char in s:
            # If the current character is a digit
            if char.isdigit() and answer:
                # If the answer list is not empty, remove the last character
                answer.pop()
            else:
                # If the character is not a digit, add it to the answer list
                answer.append(char)

        # Join the list back into a string before returning
        return "".join(answer)


class SolutionInPlace:
    def clearDigits(self, s: str) -> str:
        # This variable keeps track of the actual length of the resulting string
        answer_length = 0
        s = list(s)

        # Iterate through each character in the input string
        for char_index in range(len(s)):

            # If the current character is a digit
            if s[char_index].isdigit():
                # Decrement answerLength to remove the last character from the result
                answer_length = max(answer_length - 1, 0)
            else:
                # Place the character in the "answer" portion of the string
                s[answer_length] = s[char_index]
                answer_length += 1

        # Resize the string to match the actual length of the answer
        s = s[:answer_length]

        return "".join(s)
