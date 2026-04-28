class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """

        k-sized sliding window of len(s1)

        permutation means same freq_lists

        1. create s1_freq_list
        2. sliding window
        - window is a freq_list
        - matches algo, calculate initial matches before sliding window
        - if window == s1_freq_list (matches algo) --> permutation found
        

                        0
        s1_freq_list = [1, 1, 1, 0, 0,..., 0]
        window =       [1, 1, 1, 0, 0... , 0]

        """

        # create s1_freq_list
        s1_freq_list = [0] * 26
        for c in s1:
            s1_freq_list[ord(c)-ord('a')] += 1

        # k-size sliding window
        window = [0] * 26
        L = 0
        k = len(s1)

        # calculate initial matches
        matches = 0
        for i in range(len(s1_freq_list)):
            if s1_freq_list[i] == window[i]:
                matches += 1
        
        for R in range(len(s2)):
            # expand
            if window[ord(s2[R])-ord('a')] == s1_freq_list[ord(s2[R])-ord('a')]:
                matches -= 1
            window[ord(s2[R])-ord('a')] += 1
            if window[ord(s2[R])-ord('a')] == s1_freq_list[ord(s2[R])-ord('a')]:
                matches += 1

            # shrink
            while R-L+1 > k:
                if window[ord(s2[L])-ord('a')] == s1_freq_list[ord(s2[L])-ord('a')]:
                    matches -= 1
                window[ord(s2[L])-ord('a')] -= 1
                if window[ord(s2[L])-ord('a')] == s1_freq_list[ord(s2[L])-ord('a')]:
                    matches += 1
                
                L += 1

            # update - check matches
            if matches == 26:
                return True
        
        return False




