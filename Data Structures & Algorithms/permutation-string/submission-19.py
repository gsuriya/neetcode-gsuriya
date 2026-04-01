class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        k = len(s1)

        s1 = aabc

        s2 = acb

        """


        # make s1_map
        s1_map = defaultdict(int)
        for c in s1:
            s1_map[c] += 1
 
        # sliding window, compare windows to s1_map --> return True if same
        L = 0
        k = len(s1)

        window = defaultdict(int) # freq_map

        for R in range(len(s2)):
            # expand window
            window[s2[R]] += 1

            # condition to move L
            while R-L+1 > k:
                window[s2[L]] -= 1
                if window[s2[L]] == 0:
                    del window[s2[L]]
                L += 1

            # check equality
            if window == s1_map:
                return True

        return False



        return False