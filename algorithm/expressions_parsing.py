
class BraketsValidator(object):

    def __init__(self, opening=['{', '[', '('], closing=['}', ']', ')']):
        self.opening = opening
        self.closing = closing

    def is_opening(self, c):
        return c in self.opening
    
    def is_closing(self, c):
        return c in self.closing
    
    def ends_match(self, opening, closing):
        result = opening == '{' and closing == '}'
        result = result or (opening == '(' and closing == ')')
        result = result or (opening == '[' and closing == ']')
        return result
    
    def is_valid(self, expression):
        stack = []
        for c in expression:
            if self.is_opening(c):
                stack.append(c)
            if self.is_closing(c):
                if len(stack) == 0:
                    return False

                bracket = stack.pop()
                if self.is_closing(bracket):
                    return False

                if not self.ends_match(bracket, c):
                    return False

        return len(stack) == 0
