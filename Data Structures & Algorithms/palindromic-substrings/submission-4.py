class Solution:
    def countSubstrings(self, s: str) -> int:
        """

        count even and odd palindromes

        """

        res = 0

        for i in range(len(s)):
            # odd palindromes
            L, R = i, i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                res += 1
                L -= 1
                R += 1

            # even palindromes
            L, R = i, i+1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                res += 1
                L -= 1
                R += 1
        
        return res