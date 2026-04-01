class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        reg = []
        for c in s:
            stack.append(c)
            reg.append(c)

        """
        "Was it a car or a cat I saw?"

        stack = [Was it a car or a cat I saw]

                 i
        reg =   [Was it a car or a cat I saw?]
        """

        # compare equality
        i = 0
        while stack:
            while stack and not self.is_alphanum(stack[-1]):
                stack.pop()
            while i < len(reg) and not self.is_alphanum(reg[i]):
                i += 1

            if stack and stack.pop().lower() != reg[i].lower():
                return False
            i += 1
        
        return True
    
    def is_alphanum(self, c):
        if (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')) or (ord('0') <= ord(c) <= ord('9')):
            return True
        return False
            