class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        dynamically updating max: longest_str

        GPT: two ways to do this
        1. delete from window as L moves
        2. never delete from window, jump L with max idiom
        
        L     R
        x z y z x y z

        if R in window:
            longest_str = max(R-L, longest_str)
            L moves to 1 + wherever dup is
        """

        window = {} # char --> index
        L = 0
        longest_str = 0

        for R in range(len(s)):
            if s[R] in window:
                # iterate L to there removing the numbers in between from window
                index = window[s[R]] + 1
                while L != index:
                    del window[s[L]]
                    L += 1

            longest_str = max(R-L+1, longest_str)

            window[s[R]] = R # add to window
        
        return longest_str

