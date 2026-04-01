class Solution:
    def isValid(self, s: str) -> bool:
        # if open bracket, add to stack

        # if closed bracket, check if matches top of stack
        # - if yes, then pop top of stack
        # - if no, then return False

        stack = []
        close_to_open = {'}':'{', ']':'[', ')':'('}

        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if stack:
            return False
        
        return True
            