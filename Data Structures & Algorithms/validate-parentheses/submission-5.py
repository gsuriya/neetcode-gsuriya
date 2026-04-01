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
        
        if len(stack) == 0:
            return True
        else: 
            return False # if only one opening was added to stack, then you know that string is invalid
