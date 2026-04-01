class Solution:
    def isValid(self, s: str) -> bool:
        """

        add openings to stack
        check closings w/ top of stack

        if openings left in stack, return False
        if stack empty and closing, return False

        """

        closed_to_open = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []

        for c in s:
            # closing --> check w/ top of stack
            if c in closed_to_open:
                if not stack or stack[-1] != closed_to_open[c]:
                    return False
                stack.pop()
            
            # opening --> add to stack
            else:
                stack.append(c)
        
        if stack:
            return False
        
        return True


