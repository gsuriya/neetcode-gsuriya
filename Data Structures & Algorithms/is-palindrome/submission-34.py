class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # move them to alphanumeric characters
            while l < r and not self.is_alphanum(s[l]):
                l += 1
            while r > l and not self.is_alphanum(s[r]):
                r -= 1

            # check equality
            if s[l].lower() != s[r].lower():
                return False

            # move pointers
            l += 1
            r -= 1

        return True

    def is_alphanum(self, c):
        if (ord('a') <= ord(c.lower()) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')):
            return True
        return False 
            