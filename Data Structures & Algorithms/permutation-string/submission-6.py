class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # make map of s1
        s1_freq_map = defaultdict(int)
        for char in s1:
            s1_freq_map[char] += 1

        # sliding window k = len(s1), check that window freq_map == s1_map
        L = 0
        window_freq_map = defaultdict(int)
        k = len(s1)

        for R in range(len(s2)):
            # expand window
            window_freq_map[s2[R]] += 1

            # fixed window size k
            while R-L+1 > k:
                window_freq_map[s2[L]] -= 1
                if window_freq_map[s2[L]] == 0: # if decrementing causes 0 freq, remove K-V pair
                    del window_freq_map[s2[L]]
                L += 1
            
            if window_freq_map == s1_freq_map:
                return True
        
        return False

