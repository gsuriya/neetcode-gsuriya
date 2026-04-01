class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(1) space, so no auxiliary data structures like stack or another array allowed
        # only way to do that is to use two pointers

        L = 0
        R = len(s)-1
 
        while L < R:
            # ignore non-alphanumeric characters, keep moving L and R pointers
            while L < R and not self.isalphanum(s[L]):
                L += 1
            while L < R and not self.isalphanum(s[R]):
                R -= 1

            if s[L].lower() != s[R].lower():
                return False

            L += 1
            R -= 1
        return True

    def isalphanum(self, char):
        return (ord("a") <= ord(char) <= ord("z")
        or ord("A") <= ord(char) <= ord("Z")
        or ord("0") <= ord(char) <= ord("9"))