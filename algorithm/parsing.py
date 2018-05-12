def is_opening(c):
    return c == '{' or c == '[' or c == '('

def is_closing(c):
    return c == '}' or c == ']' or c == ')'

def matches(opening, closing):
    result = opening == '{' and closing == '}'
    result = result or (opening == '(' and closing == ')')
    result = result or (opening == '[' and closing == ']')
    return result

def is_matched(expression):
    stack = []
    for c in expression:
        if is_opening(c):
            stack.append(c)
        if is_closing(c):
            if len(stack) == 0:
                return False

            bracket = stack.pop()
            if is_closing(bracket):
                return False

            if not matches(bracket, c):
                    return False

    return len(stack) == 0
