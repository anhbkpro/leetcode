def calculate(exp: str) -> int:
    """
    This is a simple calculator that evaluates expressions with nested parentheses.
    It supports two operators: "add" and "mul".
    It handles nested expressions correctly.
    It raises an error if the expression is invalid.
    It raises an error if the expression is empty.
    It raises an error if the expression is not a valid expression.
    It raises an error if the expression is not a valid expression.
    """

    def evaluate(tokens):
        if not tokens:
            raise ValueError("Empty expression")

        # Get the operator
        if not tokens or tokens[0] not in ["add", "mul"]:
            raise ValueError(
                f"Invalid or missing operator: {tokens[0] if tokens else 'None'}"
            )

        operator = tokens[0]

        # Get the operands
        operands = []
        i = 1
        while i < len(tokens):
            if tokens[i] == "(":
                # Find the matching closing parenthesis
                count = 1
                j = i + 1
                while j < len(tokens) and count > 0:
                    if tokens[j] == "(":
                        count += 1
                    elif tokens[j] == ")":
                        count -= 1
                    j += 1
                if count > 0:
                    raise ValueError("Unmatched parentheses")
                # Recursively evaluate the nested expression
                operands.append(evaluate(tokens[i + 1 : j - 1]))
                i = j
            else:
                # Handle numbers (including negative numbers)
                if tokens[i].isdigit() or (
                    tokens[i].startswith("-") and tokens[i][1:].isdigit()
                ):
                    operands.append(int(tokens[i]))
                i += 1

        # Check for missing operands
        if len(operands) < 2:
            raise ValueError(f"Missing operands for operator {operator}")

        # Perform the operation
        if operator == "add":
            return sum(operands)
        elif operator == "mul":
            result = 1
            for operand in operands:
                result *= operand
            return result

    # Tokenize the input
    if not exp.strip():
        raise ValueError("Empty expression")

    tokens = []
    i = 0
    while i < len(exp):
        if exp[i] == " ":
            i += 1
        elif exp[i] in "()":
            tokens.append(exp[i])
            i += 1
        else:
            # Read a complete token (word or number)
            j = i
            while j < len(exp) and exp[j] not in "() ":
                j += 1
            tokens.append(exp[i:j])
            i = j

    # Validate basic structure
    if not tokens or tokens[0] != "(" or tokens[-1] != ")":
        raise ValueError("Invalid expression format")

    # Remove outer parentheses and evaluate
    return evaluate(tokens[1:-1])


# Test the functions
if __name__ == "__main__":
    test_cases = [
        "( add 2 5 )",  # Expected: 7
        "( mul 2 4 )",  # Expected: 8
        "( add 2 ( mul 2 2 ) )",  # Expected: 6
        "( mul ( mul 2 2 ) ( add 1 3 ) )",  # Expected: 16
    ]

    print("Testing approach:")
    for test in test_cases:
        try:
            result = calculate(test)
            print(f"{test} -> {result}")
        except Exception as e:
            print(f"{test} -> Error: {e}")
