class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """

        instead of k constant size sliding window

        expand
        shrink when window is VALID
        - UPDATE FIRST when window is considered valid before shrinking

        """
        # edge case
        if len(t) > len(s): # all the chars of t can't be in s
            return ""

        t_freq = {}
        for c in t:
            if c not in t_freq:
                t_freq[c] = 0
            t_freq[c] += 1
        
        window = {}

        matches = 0

        L = 0
        length = float('inf')
        fL, fR = 0, 0

        for R in range(len(s)):
            # expand
        
            
            if s[R] not in window:
                window[s[R]] = 0
            window[s[R]] += 1
            
            #   equal after, incrementing caused match
            if s[R] in window and s[R] in t_freq and window[s[R]] == t_freq[s[R]]:
                matches += 1

            # shrink - if window valid
            # - update
            while matches == len(t_freq):
                if R-L+1 < length:
                    length = R-L+1
                    fL, fR = L, R
                
                #   equal now, decrementing causes mismatch
                if s[L] in window and s[L] in t_freq and window[s[L]] == t_freq[s[L]]:
                    matches -= 1
               
                window[s[L]] -= 1
                if window[s[L]] == 0: # get rid of chars w/ freq 0
                    del window[s[L]] 
                
              
                L += 1


        return "" if length == float('inf') else s[fL:fR+1]








