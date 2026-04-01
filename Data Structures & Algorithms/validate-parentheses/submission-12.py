class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")":"(", "}":"{", "]":"["}
        stack = []

        for c in s:
            # if c closing, check if top of stack matches; if not -> false
            if c in close_to_open.keys():
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False

            # if c opening, add to stack
            else:
                stack.append(c)

        
        # if stack empty -> true; if not -> false
        # stack having things means openings weren't matched
        if stack:
            return False
        else:
            return True


        
