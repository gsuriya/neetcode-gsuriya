class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """

        k=len(s1) size sliding window_freq_map on s2

        check equality of hashmaps using matches method

        note: only lowercase english alphabet so freq_arr size 26
        s1_arr = [1, 1, 1, 0, 0, 0,...]
        s2_arr = [0, 0, 0, 0, 0, 0,...

        matches = 23

        1. construct freq_arrs and get initial matches
        2. k size sliding window w/ matches hashmap equality comparison 

        """

        # 1. construct freq_arrs and get initial matches
        s1_freq = [0] * 26
        for c in s1:
            s1_freq[ord(c)-ord('a')] += 1
        window = [0] * 26 # s2_freq map

        matches = 0
        for i in range(len(s1_freq)):
            if s1_freq[i] == window[i]:
                matches += 1
        
        # 2. k size sliding window
        k = len(s1)
        L = 0
        
        for R in range(len(s2)):
            # expand
            if window[ord(s2[R])-ord('a')] == s1_freq[ord(s2[R])-ord('a')]:
                matches -= 1
            window[ord(s2[R])-ord('a')] += 1
            if window[ord(s2[R])-ord('a')] == s1_freq[ord(s2[R])-ord('a')]:
                matches += 1
            
            # shrink - window size larger than k
            while (R-L+1) > k:
                if window[ord(s2[L])-ord('a')] == s1_freq[ord(s2[L])-ord('a')]:
                    matches -= 1
                window[ord(s2[L])-ord('a')] -= 1
                if window[ord(s2[L])-ord('a')] == s1_freq[ord(s2[L])-ord('a')]:
                    matches += 1

                L += 1

            # check hashmap equality
            if matches == 26: # freq arrs hv to be exact same
                return True
        
        return False
        




