class Solution:
    def isValid(self, s: str) -> bool:
        """

        add openings to the stack        
        closings check w/ top of stack

        """

        close_to_open = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        stack = []

        for c in s:
            # closing
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False

            # opening
            else:
                stack.append(c)
        
        # openings left remaining in stack
        if stack:
            return False
        
        return True

        