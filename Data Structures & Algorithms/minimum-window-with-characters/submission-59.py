class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """

        use hashmaps instead since no "before check" 
        and size 54 lists needed

        sliding window

        t_map = {
            c: 1
            a: 1
            e: 1
        }

        L R
        c a b w e f g e w c w a e f g c f

        window = {
            c: 1
            a: 1
        }
        """
        min_length = float('inf')
        fL, fR = 0, 0

        t_map = {}
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        
        window = {} # s_map
        L = 0
        matches = 0
        
        for R in range(len(s)):
            # expand
            window[s[R]] = window.get(s[R], 0) + 1
            if s[R] in t_map and window[s[R]] == t_map[s[R]]:
                matches += 1

            # shrink - since we hv all letters
            while matches == len(t_map):
                # update
                if min_length > R-L+1:
                    min_length = R-L+1
                    fL, fR = L, R

                if s[L] in t_map and window[s[L]] == t_map[s[L]]:
                    matches -= 1
                window[s[L]] -= 1
                L += 1
        
        return s[fL:fR+1] if min_length != float('inf') else ""
        

        



        