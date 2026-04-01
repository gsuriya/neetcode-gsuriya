class Solution:
    def countSubstrings(self, s: str) -> int:
        """

        ODD palindromes

        EVEN palindromes

        """
        count = 0

        for center in range(len(s)):
            # odd
            L, R = center, center
            while L >= 0 and R < len(s) and s[L] == s[R]:
                count += 1
                L -= 1
                R += 1

            # even
            L, R = center, center+1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                count += 1
                L -= 1
                R += 1

        return count
