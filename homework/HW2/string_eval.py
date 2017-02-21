def string_eval(expr):
    """
    @type expr: string
    @param expr: A valid arithmetic expression containing only "+", "-", and
    "*" operators, no parentheses, non-negative operands

    @rtype: int
    @return: The result of evaluating expr from left to right, following order
    of operations.
    """

    return result

if __name__ == "__main__":
    test_input_1 = "2+3*4-8"
    print("Input:", test_input_1)
    print("Your output:", string_eval(test_input_1))
    print("Expected output:", 6)

    test_input_2 = "4+2"
    print("Input:", test_input_2)
    print("Your output:", string_eval(test_input_2))
    print("Expected output:", 6)
