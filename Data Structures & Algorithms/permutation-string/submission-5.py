class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if s1 reordered in s2

        # if freq_map s1 in s2 substring

        # option 1: check freq_map of every s2 substring O(N^2)

        # option 2: use sliding window to check substrings, decreasing to O(N)
        # -- now, what is the WC and what cases do we slide the window?

        # ok so can't check entire s2 against s1 b/c permutation means SUBSTRING so freq letters need to be
        # NEXT to each other in s2 --> still check freq_map of each substring approach

        """
        Q: how do you expand/shrink window so that it gets closer to substring freq_map of s1??
        -   bro use fixed window size of len(s1) dumbass

        s1 = abc

             
             R
             L       
        s2 = l e c a b e e

        window represents freq_map of current substring
        window_freq_map {
            
        }

        """

        if len(s1) > len(s2):
            return False

        s1_freq_map = defaultdict(int)
        for char in s1:
            s1_freq_map[char] += 1

        L = 0
        freq_map = defaultdict(int)
        k = len(s1)

        for R in range(len(s2)):
            # expand window
            freq_map[s2[R]] += 1

            # keep moving R unless over window size
            while (R-L+1) > k:
                freq_map[s2[L]] -= 1
                if freq_map[s2[L]] == 0:
                    del freq_map[s2[L]]
                L += 1
            
            # check if freq_map of window is equal to s1_freq_map
            if freq_map == s1_freq_map:
                return True
        
        return False











