class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer approach
        L , R = 0, len(s)-1


        while L <= R:
            # move L to alphanumeric
            while L < R and not self.is_alphanumeric(s[L]):
                L += 1

            # move R to alphanumeric
            while L < R and not self.is_alphanumeric(s[R]):
                R -= 1

            # if its equal, continue else return False
            if s[L].lower() != s[R].lower():
                return False 

            L += 1
            R -= 1

        # if not return false from above, ur good
        return True

    # helper function to determine if its alphanumeric or not
    def is_alphanumeric(self, char):
        # A-Z, a-z, 0-9
        if (ord('A') <= ord(char) <= ord('Z') or
        ord('a') <= ord(char) <= ord('z') or
        ord('0') <= ord(char) <= ord('9')):
            return True
        return False
