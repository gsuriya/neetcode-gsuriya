class Solution:
    def isValid(self, s: str) -> bool:
        """

        [{()}]

        [(])

        ]]]]

        stack = [
            
        ]

        if open: 
            - add to stack
        if close:
            - check if stack[-1] == open version of closing

        if len(stack) > 0 at end, then must mean not all opens were popped by corresponding closed
            - return False

        """
        stack = []
        close_to_open = {"}":"{", ")":"(","]":"["}

        for char in s:
            if char in close_to_open:
                if stack and close_to_open[char] == stack[-1]:
                    stack.pop()
                else:
                    return False # if opening doesn't match closing
            else:
                stack.append(char)
        
        if len(stack) > 0:
            return False
        
        return True

