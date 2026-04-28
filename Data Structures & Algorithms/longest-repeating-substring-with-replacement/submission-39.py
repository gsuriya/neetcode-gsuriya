class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """

        A A A B A B B

        k = 2

        - replace char w/ least frequency
        - longest_str = max(freq) + k

        freq_map = {
            A: 4
            B: 1
            C: 1
        }

        (R-L+1) - max(freq_map.values()) > k

        if rest of chars every get GREATER than k, then need to cut down

        max_length = highest freq + k

        """

        L = 0
        window = defaultdict(int) # char --> freq
        max_length = 0
        maxf = 0

        for R in range(len(s)):
            # expand
            window[s[R]] += 1
            maxf = max(maxf, window[s[R]])

            # shrink - while rest of chars greater than k
            while R-L+1 - maxf > k:
                window[s[L]] -=1
                L += 1

            # update
            max_length = max(max_length, R-L+1)
        
        return max_length





