class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(1) space, so use TWO POINTERS
        L = 0
        R = len(s)-1

        # case-insensitive and ignored non-alphanumeric characters
        while L <= R:
            # loop L and R to alphanumeric character
            while not self.is_alphanumeric(s[L]) and L < R:
                L += 1
            while not self.is_alphanumeric(s[R]) and L < R:
                R -= 1

            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1

        return True

    def is_alphanumeric(self, s: str):
        if ((ord("A") <= ord(s) <= ord("Z")) or
            (ord("a") <= ord(s) <= ord("z")) or
            (ord("0") <= ord(s) <= ord("9"))):
            return True
        
        return False