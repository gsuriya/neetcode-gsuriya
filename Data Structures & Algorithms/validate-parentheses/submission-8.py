class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            # if char is closing, check if corresponding open in stack
            if char in closeToOpen.keys():
                if len(stack) > 0 and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            # if char is opening, append to stack
            else:
                stack.append(char)
        
        # if not all openings were removed from stack by corresponding closings
        if stack:
            return False
        else:
            return True
