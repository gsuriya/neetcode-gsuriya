class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """

        substring - sliding windo

        L     R
        z x y z x y z

        check if R in window (set)
        - if yes --> move L until s[R] out of window

        """

        L = 0
        window = set()
        max_length = 0

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1

            # expand - now valid to add
            window.add(s[R])
            
            # update
            max_length = max(max_length, R-L+1)
            
        return max_length



