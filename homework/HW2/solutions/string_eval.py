def has_precedence(op1, op2):
    if op2 == "*":
        if op1 == "*":
            return True
        else:
            return False
    else:
        return True

def string_eval(expr):
    """
    @type expr: string
    @param expr: A valid arithmetic expression containing only "+", "-", and
    "*" operators, no parentheses, non-negative operands

    @rtype: int
    @return: The result of evaluating expr from left to right, following order
    of operations.
    """

    # break the expression up into tokens
    tokenized_expr = []
    i = 0
    while i < len(expr):
        token = ""
        if expr[i].isdigit():
            while i < len(expr) and expr[i].isdigit():
                token += expr[i]
                i += 1
        else:
            token = expr[i]
            i += 1
        tokenized_expr.append(token)

    postfix_expr = []
    operator_stack = []

    # convert to postfix
    for token in tokenized_expr:
        if token.isdigit():
            postfix_expr.append(token)
        else:
            while operator_stack and has_precedence(operator_stack[-1],
                    token):
                postfix_expr.append(operator_stack.pop())
            operator_stack.append(token)

    while operator_stack:
        postfix_expr.append(operator_stack.pop())

    result = []
    postfix = postfix_expr[::-1]
    # evaluate
    
    while postfix:
        if postfix[-1].isdigit():
            result.append(postfix.pop())
        else:
            operator = postfix.pop()
            op1 = result.pop()
            op2 = result.pop()
            if operator == "-":
                result.append(int(op2) - int(op1))
            elif operator == "+":
                result.append(int(op2) + int(op1))
            else:
                result.append(int(op2) * int(op1))

    return int(result[0])

if __name__ == "__main__":
    test_input_1 = "2+3*4-8"
    print("Input:", test_input_1)
    print("Your output:", string_eval(test_input_1))
    print("Expected output:", 6)

    test_input_2 = "3+49-3*4"
    print("Input:", test_input_2)
    print("Your output:", string_eval(test_input_2))
    print("Expected output:", 40)
