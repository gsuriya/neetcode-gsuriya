class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """

        if new character in set, 
        --> keep removing until character gone

        """

        L = 0
        window = set()
        max_length = 0
        
        for R in range(len(s)):
            # shrink window
            while s[R] in window:
                window.remove(s[L])
                L += 1

            # update length
            max_length = max(max_length, R-L+1)

            # add to window
            window.add(s[R])
        
        return max_length

            

            

            