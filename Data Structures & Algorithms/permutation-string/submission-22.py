class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        O(26n) --> O(n)
        goal: make comparing freq_maps O(1) --> use matches counter
        """
        
        # s1 to freq_map
        s1_freq_arr = [0] * 26
        for char in s1:
            s1_freq_arr[ord(char) - ord('a')] += 1

        # sliding window of k = len(s1)
        k = len(s1)
        L = 0
        window_freq_arr = [0] * 26

        # get current matches, update matches cumulatively later
        matches = 0
        for i in range(len(s1_freq_arr)):
            matches += (1 if s1_freq_arr[i] == window_freq_arr[i] else 0)

        for R in range(len(s2)):
            # expand window
            i = ord(s2[R]) - ord('a')

            # -- case 1: equal before and incrementing caused mismatch
            if window_freq_arr[i] == s1_freq_arr[i]:
                matches -= 1

            # -- case 2: not equal before and incrementing caused match
            window_freq_arr[i] += 1
            if window_freq_arr[i] == s1_freq_arr[i]:
                matches += 1

            # shrink window over window size k
            while (R-L+1) > k:
                j = ord(s2[L]) - ord('a')
                
                # update matches
                # -- case 1: equal before and decrementing caused mismatch
                if window_freq_arr[j] == s1_freq_arr[j]:
                    matches -= 1

                # -- case2: not equal before and decrementing caused match
                window_freq_arr[j] -= 1
                if window_freq_arr[j] == s1_freq_arr[j]:
                    matches += 1
            
                L += 1

            # compare freq_arr equality
            if matches == 26:
                return True
            
        return False

        











