class Solution:
    def isValid(self, s: str) -> bool:
        """

        ([{}])

        if opening --> add to stack
        if closing --> does closing match top of stack?
             - if not, false

        if stack still has elems --> not all openings were closed
             - return false

        """

        stack = []
        close_to_open = {"}":"{", ")":"(", "]":"["}
        
        for c in s:
            # if opening
            if c not in close_to_open.keys():
                stack.append(c)
            # if closing
            else:
                if not stack or close_to_open[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        if stack:
            return False
        
        return True
