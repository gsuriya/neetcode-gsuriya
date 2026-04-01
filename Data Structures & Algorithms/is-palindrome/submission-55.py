class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s)-1

        while L < R:
            # move L and R to alphanumeric
            while L < R and not self.is_alpha(s[L]):
                L += 1
            while L < R and not self.is_alpha(s[R]):
                R -= 1 

            # compare
            if s[L].lower() != s[R].lower():
                return False

            # increment pointers
            L += 1
            R -= 1
        
        return True
        

    def is_alpha(self, c):
        if (ord("0") <= ord(c) <= ord("9") or
            ord('a') <= ord(c.lower()) <= ord('z')):
            return True

        return False
        
            