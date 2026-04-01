class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        window = set()
        length = 0

        for R in range(len(s)):
            # shrink window
            while s[R] in window:
                window.remove(s[L])
                L += 1

            # expand window
            window.add(s[R])

            # update
            length = max(length, R-L+1)
        
        return length

