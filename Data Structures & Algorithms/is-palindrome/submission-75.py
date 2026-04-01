class Solution:
    def isPalindrome(self, s: str) -> bool:
        """

        skip non-alphanumeric chars
        - use helper 

        L                         R
        Was it a car or a cat I saw?

        """

        L, R = 0, len(s)-1

        while L <= R:
            # move to an alphanumeric char
            while L < R and not self.is_alpha(s[L]):
                L += 1
            while L < R and not self.is_alpha(s[R]):
                R -= 1
            
            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1
        
        return True

    def is_alpha(self, c):
        if ((ord('a') <= ord(c.lower()) <= ord('z')) or
            ord('0') <= ord(c) <= ord('9')):
            return True
        return False



