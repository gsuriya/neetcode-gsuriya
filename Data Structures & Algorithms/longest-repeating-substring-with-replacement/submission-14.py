class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # substring --> sliding window algo
        # WC: freq of least freq char <= k
        # to get largest substring, swap LEAST FREQ letters --> use freq_map
        L = 0 
        freq_map = defaultdict(int)
        longest_str = 0 # dynamic max

        for R in range(len(s)):
            # expand window, add to map
            freq_map[s[R]] += 1

            # if WC false --> while loop to move L to make it true again
            while (R-L+1) - max(list(freq_map.values())) > k:
                freq_map[s[L]] -= 1
                L += 1

            # update max
            longest_str = max(R-L+1 , longest_str)
        
        return longest_str

            