class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
              R
            L     
        x z y z
        
        expand window - R moves
        condition to move L - L = dup + 1
        update value - longest_str


        """
    
        L = 0
        c_map = {} # char --> index
        longest_str = 0

        for R in range(len(s)):
            if s[R] in c_map: # duplicate found
                # L = dup + 1, remove window on the way
                index = c_map[s[R]] + 1
                while L != index:
                    del c_map[s[L]]
                    L += 1

            # expand window
            c_map[s[R]] = R
            
            longest_str = max(longest_str, R-L+1)
        
        return longest_str


