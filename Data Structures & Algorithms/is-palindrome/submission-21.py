class Solution:

    """
     l                       r  
    Was it a car or a cat I saw?
    """

    def isPalindrome(self, s: str) -> bool:
        # two pointer approach
        l, r = 0, len(s)-1

        while l <= r:
            # move l and r to an alphanumeric
            while l < r and not self.is_alphanumeric(s[l]):
                l += 1
            while l < r and not self.is_alphanumeric(s[r]):
                r -= 1    

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True


    def is_alphanumeric(self, c):
        # if c is num or letter
        if (ord('a') <= ord(c.lower()) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')):
            return True
        return False