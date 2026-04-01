class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # window condition means no duplicates

        window = {} # char --> index
        L = 0
        max_length = 0
        for R in range(len(s)):
            if s[R] in window:
                # duplicate found --> move L to window[s[R]] + 1 and remove from map along the way
                index = window[s[R]] + 1
                while L != index:
                    del window[s[L]]
                    L += 1

            window[s[R]] = R
            max_length = max(R-L+1, max_length)
        
        return max_length



        """
        window = {x:0 y:1 z:2}


        L     R
        x y z y



        """

