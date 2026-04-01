class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 to freq_map
        s1_freq_map = {}
        for char in s1:
            s1_freq_map[char] = s1_freq_map.get(char, 0) + 1

        # sliding window of k = len(s1)
        k = len(s1)
        L = 0
        window_freq_map = {}

        for R in range(len(s2)):
            # expand window
            window_freq_map[s2[R]] = window_freq_map.get(s2[R], 0) + 1

            # shrink window over window size k 
            while (R-L+1) > k:
                window_freq_map[s2[L]] -= 1
                if window_freq_map[s2[L]] == 0:
                    del window_freq_map[s2[L]] # so equality check not messed up
                L += 1

            # if freq_maps equal, valid substring permutation so return True
            if window_freq_map == s1_freq_map:
                return True
        
        return False

        











