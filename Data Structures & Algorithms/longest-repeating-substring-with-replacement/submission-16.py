class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """

        find largest substring --> sliding window algo
        - have a window condition and keep expanding, updating res
        - if window condition is false, shrink window until true again
        - therefore, ensures largest widow size with condition found

        WC:
        - # of chars to replace <= k
        - # chars to replace = window size - freq of most common letter
        - # chars to replace = (R-L+1) - maxf

        - res = maxf + k
        therefore, res is maximized when maxf is
        EUREKA: we don't care ab decrementing maxf cus res aint 
        updating anyways when res is lower, k is CONSTANT so res
        is only dependent on maxf being larger

        """

        L = 0
        window = defaultdict(int) # letter --> freq
        length = 0 # res dynamically updating max
        maxf = 0

        for R in range(len(s)):
            # expand window
            window[s[R]] += 1
            maxf = max(maxf, window[s[R]])
            
            # shrink window
            while (R-L+1) - maxf > k:
                window[s[L]] -= 1
                L += 1
            
            # update
            length = max(length, R-L+1)
        
        return length








