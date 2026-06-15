class Solution:
    def countSubstrings(self, s: str) -> int:
        """

        iterate thru
        - expand outwards for even AND odd palis
        - if pali found --> increment count

        """

        count = 0
        
        for i in range(len(s)):
            # expand outwards for odd palindromes
            L, R = i, i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                count += 1
                L -= 1
                R += 1

            # expand outwards for even palindromes
            L, R = i, i+1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                count += 1
                L -= 1
                R += 1
        
        return count

