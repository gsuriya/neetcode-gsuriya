class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """

        compare freq_lists

        s1_freq = [1, 1, 1, 0, 0,...]

        window = [0, 0, 0, 0,...]

          L   R
        l e c a b e e

        """

        s1_freq = [0] * 26
        for c in s1:
            s1_freq[ord(c)-ord('a')] += 1
        
        # sliding window
        L = 0
        window = [0] * 26
        k = len(s1)
        
        matches = 0
        for i in range(len(s1_freq)):
            if s1_freq[i] == window[i]:
                matches += 1

        for R in range(len(s2)):
            # expand
            if window[ord(s2[R])-ord('a')] == s1_freq[ord(s2[R])-ord('a')]:
                matches -= 1
            window[ord(s2[R])-ord('a')] += 1
            if window[ord(s2[R])-ord('a')] == s1_freq[ord(s2[R])-ord('a')]:
                matches += 1

            # shrink
            while R-L+1 > k:
                if window[ord(s2[L])-ord('a')] == s1_freq[ord(s2[L])-ord('a')]:
                    matches -= 1
                window[ord(s2[L])-ord('a')] -= 1
                if window[ord(s2[L])-ord('a')] == s1_freq[ord(s2[L])-ord('a')]:
                    matches += 1
                L += 1

            # update
            if matches == 26:
                return True
        
        return False





