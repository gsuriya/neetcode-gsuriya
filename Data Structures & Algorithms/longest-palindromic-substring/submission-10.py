class Solution:
    def longestPalindrome(self, s: str) -> str:
        """

        iterate thru s
        - expand outwards while L and R same
        - update max_length

        """

        max_length = 1
        res = ""

        for i in range(len(s)):
            # expand outwards
            L, R = i, i

            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R-L+1 >= max_length:
                    max_length = R-L+1
                    res = s[L:R+1]
                
                L -= 1
                R += 1
            
            L, R = i, i+1

            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R-L+1 > max_length:
                    max_length = R-L+1
                    res = s[L:R+1]
                
                L -= 1
                R += 1

        return res


