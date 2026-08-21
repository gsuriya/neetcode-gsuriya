class Solution:
    def isValid(self, s: str) -> bool:
        """

        opening --> add to stack
        closing --> check w/ top

        """

        close_to_open = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        stack = []

        for c in s:
            if c in close_to_open: # closing
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False

            else: # opening
                stack.append(c)

        # still openings left
        if stack:
            return False
        
        return True