import A_stack

def check_braces_sequence(s):
    """
    Проверяет корректность скобочной последовательности 
    из круглых () и квадратных [] скобок

    >>> check_braces_sequence("[]")
    True
    >>> check_braces_sequence("([)]")
    False
    >>> check_braces_sequence("(")
    False
    >>> check_braces_sequence("]")
    False
    """

    for brace in s:
        if brace not in '()[]':
            continue
        if brace in "([":
            A_stack.push(brace)
        else:
            #assert brace in ")]"
            if A_stack.is_empty():
                return False
            left = A_stack.pop()
            #assert left in "(["
            if left == "(":
                right = ")"
            elif left == "[":
                right == "]"
            if right != brace:
                return False
    return A_stack.is_empty()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
