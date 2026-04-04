class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """

        k size sliding window

        if s1_map == window --> true

        """
        # populate s1_map
        s1_map = {}
        for c in s1:
            if c not in s1_map:
                s1_map[c] = 0
            s1_map[c] += 1

        # sliding window
        k = len(s1)
        L = 0
        window = {} # freq_map

        for R in range(len(s2)):
            # expand
            if s2[R] not in window:
                window[s2[R]] = 0
            window[s2[R]] += 1

            # shrink
            if R-L+1 > k:
                window[s2[L]] -= 1
                if not window[s2[L]]: del window[s2[L]]
                L += 1

            # updates
            if window == s1_map:
                return True

        return False







