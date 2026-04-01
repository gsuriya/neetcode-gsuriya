class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """

        1. create freq_maps for s1 and window

        2. k size sliding window: return true if freq_maps equal
        - use matches algo

        s1 = ab
        s2 = lecabee

        s1_freq = [1, 1, 24 0's]

        """

        L = 0
        window = [0] * 26
        k = len(s1)

        s1_freq = [0] * 26
        for c in s1:
            s1_freq[ord(c)-ord('a')] += 1

        # instantiate initial matches
        matches = 0
        for i in range(len(s1_freq)):
            if s1_freq[i] == window[i]:
                matches += 1

        for R in range(len(s2)):    
            # EXPAND
            #   equal now, incrementing causeses mismatch
            if window[ord(s2[R])-ord('a')] == s1_freq[ord(s2[R])-ord('a')]: 
                matches -= 1
            window[ord(s2[R])-ord('a')] += 1
            #   equal now, incrementing made a match
            if window[ord(s2[R])-ord('a')] == s1_freq[ord(s2[R])-ord('a')]: 
                matches += 1

            # SHRINK
            while R-L+1 > k:
                #   equal now, decrementing causes mismatch
                if window[ord(s2[L])-ord('a')] == s1_freq[ord(s2[L])-ord('a')]:
                    matches -= 1
                window[ord(s2[L])-ord('a')] -= 1
                #   equal now, decrementing caused match
                if window[ord(s2[L])-ord('a')] == s1_freq[ord(s2[L])-ord('a')]:
                    matches += 1
                L += 1

            # update
            if matches == 26:
                return True
        
        return False




            