class Solution:
    def isValid(self, s: str) -> bool:
        """

        stack
        - if open, append
        - if closing, check top of stack

        """

        stack = []

        close_to_open = {
            ']':'[',
            '}':'{',
            ')':'('
        }

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
        
        # if openings left in stack
        if stack:
            return False
        
        return True



        



