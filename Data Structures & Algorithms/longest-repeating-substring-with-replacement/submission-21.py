class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        substring --> sliding window

          L
                  R
        A A A B A B B

        max_freq = 4

    window_freq_map = {
        A: 3
        B: 2
    }
        
        EXPAND 
        add letter to freq_map

        SHRINK while update condition is invalid
        b/c u want to replace the least frequent character in the window
        (R-L+1) - highest freq = # of letters to replace > k

        UPDATE CONDITION
        update max_length to be (R-L+1)

        max_length = highest_freq + k
        - therefore, max_length is at its highest value when highest_freq is at its highest value
        - keeping max_freq at its highest point means that all the window sizes later on
          will be at max_freq + k. so if a larger max_freq occurs, THEN the window size will expand
          and max_freq will be updated again
        """

        window = {} # letter --> freq
        L = 0
        max_length = 0
        max_freq = 0

        for R in range(len(s)):
            # expand, also update max_freq
            window[s[R]] = window.get(s[R], 0) + 1
            max_freq = max(max_freq, window[s[R]])

            # shrink - # of chars to replace exceeds chars u can replace (k)
            while (R-L+1) - max_freq > k:
                window[s[L]] -= 1
                L += 1
            
            max_length = max(max_length, R-L+1)


        return max_length




