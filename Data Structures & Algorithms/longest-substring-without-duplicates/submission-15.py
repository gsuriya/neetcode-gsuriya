class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """

        window is a set()

        before adding new char, check that its in the set alr
        keep removing from the set (incrementing L) until u 
        remove whatever R is on

          L   R
        z x y z x y z

        """

        L = 0
        window = set()
        max_length = 0
        
        for R in range(len(s)):
            # shrink
            while s[R] in window:
                window.remove(s[L])
                L += 1

            # expand
            window.add(s[R])

            # update
            max_length = max(max_length, R-L+1)
        
        return max_length




