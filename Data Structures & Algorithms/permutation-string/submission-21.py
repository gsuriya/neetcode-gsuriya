class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # make s1_map
        s1_map = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        for c in s1:
            s1_map[c] += 1


        # sliding window, compare windows to s1_map --> return True if same
        L = 0
        k = len(s1)

        window = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)} # freq_map

        # initialize matches
        matches = 0
        for key in s1_map:
            if s1_map[key] == window[key]:
                matches += 1

        for R in range(len(s2)):
            # expand window - change matches
            if s1_map[s2[R]] == window[s2[R]]:
                matches -= 1

            window[s2[R]] += 1

            if s1_map[s2[R]] == window[s2[R]]:
                matches += 1

            # condition to move L
            while R-L+1 > k:
                # change matches
                if s1_map[s2[L]] == window[s2[L]]:
                    matches -= 1

                window[s2[L]] -= 1
                
                if s1_map[s2[L]] == window[s2[L]]:
                    matches += 1

                L += 1

            # check equality
            if matches == 26:
                return True

        return False

