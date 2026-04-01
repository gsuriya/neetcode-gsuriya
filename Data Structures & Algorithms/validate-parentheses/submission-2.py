class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in closeToOpen.keys(): # if char is closing
                # if top of stack is corresponding open
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else: # if char is openning
                stack.append(char)
        
        if len(stack) == 0:
            return True
        else:
            return False
