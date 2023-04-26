
def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    stack = []
    for par in parens:
        if (par == "("):
            stack.append("(")
        elif (par == ")" and len(stack) > 0):
            if (stack.pop() != "("):
                return False
        else:
            return False
    return len(stack) == 0
