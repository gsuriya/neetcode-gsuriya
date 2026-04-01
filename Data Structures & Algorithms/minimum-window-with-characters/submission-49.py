class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """

        shortest substring of s
        - all letters of t in there

        t_map = {
            X: 1
            Y: 1
            Z: 1
        }

                      
                            R
        s = O U Z O D Y X A Z V

        window_freq_map = {
            X: 1
            A: 1
            Z: 1
        }
        
        while matches == len(t_map)
        - update
        - shrink


        matches changes when: (don't need exact freq matches, js letters to be there)
        1. after incrementing, now equal (matches += 1)
        2. equal rn, now decrementing (matches -= 1)

        """
        # create t_map
        t_map = {} # letter --> freq
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1


        # sliding window
        min_length = float('inf')
        Lf, Rf = 0, 0
        L = 0
        window = {} # letter --> freq
        matches = 0 # starts at 0 cus window map is empty

        
        for R in range(len(s)):
            # expand
            window[s[R]] = window.get(s[R], 0) + 1
            if s[R] in t_map and window[s[R]] == t_map[s[R]]:
                matches += 1

            # shrink while matches is good
            while matches == len(t_map):
                # update
                if R-L+1 < min_length: # new min_length found
                    min_length = R-L+1
                    Lf, Rf = L, R
                
                if s[L] in t_map and window[s[L]] == t_map[s[L]]:
                    matches -= 1
                window[s[L]] -= 1
                L += 1
        
        # return min_length
        return s[Lf: Rf+1] if min_length != float('inf') else ""





