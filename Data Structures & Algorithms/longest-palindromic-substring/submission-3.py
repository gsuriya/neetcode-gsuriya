class Solution:
    def longestPalindrome(self, s: str) -> str:
        """

        expand from center
        
        odd length palindromes
        - found if expanding both i and j from center

        even length palindromes
        - found if i and j one apart initially

        
        
        l c r
        a b a b d

              
        a b b c

        """
        max_length = float('-inf')
        res = [0, 0]

        for center in range(len(s)):
            # odd length palindromes
            l, r = center, center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > max_length:
                    max_length = r-l+1
                    res[0], res[1] = l, r
                l -= 1
                r += 1
                
            
            # even length palindromes
            l, r = center, center+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > max_length:
                    max_length = r-l+1
                    res[0], res[1] = l, r
                l -= 1
                r += 1

        return s[res[0]:res[1]+1]





                





