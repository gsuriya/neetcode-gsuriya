class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """

        1. freq map for t

        2. keep expanding until valid window (matches = len(t))
        - shrink until it doesn't match anymore

        expand: post-increment --> if equal: matches += 1
        shrink: pre-increment --> if equal: matches -= 1

        """
        if len(t) > len(s): # edge case cus if t is > than s then not all letters of t can be inside of s
            return ""

        t_map = {} # map b/c lowercase and uppercase letters allowed so easier
        for c in t:
            if c not in t_map:
                t_map[c] = 0
            t_map[c] += 1

        L = 0
        fl, fr = 0, 0
        window = {} # freq map
        matches = 0 # initial matches is 0 w/ an empty window freq map
        length = float('inf')

        for R in range(len(s)):
            # expand
            window[s[R]] = window.get(s[R], 0) + 1
            if s[R] in t_map and window[s[R]] == t_map[s[R]]:
                matches += 1

            # shrink
            while matches == len(t_map):
                # update b/c valid window now
                if R-L+1 < length:
                    length = R-L+1
                    fl, fr = L, R
                
                if s[L] in window and s[L] in t_map and window[s[L]] == t_map[s[L]]:
                    matches -= 1
                window[s[L]] -= 1
                if window[s[L]] == 0: del window[s[L]]

                L += 1

        return s[fl:fr+1] if length != float('inf') else ""














        
