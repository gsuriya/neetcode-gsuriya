class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """

        window = set() 

        expand: add to set

        shrink: if s[i] in nums (duplicate found)
               - keep moving L and deleting s[L] from set until its okay to add s[i] 
                 so it's not a duplicate

        """

        max_length = 0
        window = set()
        L = 0
    

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