class Solution:
    def longestPalindrome(self, s: str) -> str:
        """

        for each center, expand outward

        """
        final = [0,0]
        max_length = 0
        for center in range(len(s)):
            L, R = center, center
            # odd ones - expand L and R 
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R-L+1 > max_length:
                    max_length = R-L+1
                    final[0], final[1] = L, R
                L -= 1
                R += 1

            # even - expand L and R 
            L, R = center, center+1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R-L+1 > max_length:
                    max_length = R-L+1
                    final[0], final[1] = L, R
                L -= 1
                R += 1
        

        return s[final[0]:final[1]+1]
