class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int) # data structure for window
        L = 0
        longest_str = 0

        """
        L     R
        A B A A
        """

        for R in range(len(s)):
            # add to freq_map (keep expanding window until WC false)
            freq_map[s[R]] += 1

            # check if window constraint (window size - highest freq <= k)
            window_size = R-L+1
            highest_freq = 0
            for char in freq_map:
                highest_freq = max(freq_map[char], highest_freq)

            # -- if not, then while loop to move L until WC true
            """
            like usually u hv a while loop to move L but in this case
            it makes it like 10x harder cus u needa recalculate 
            window_size and highest_freq every time u move L so j use an 'if'

            wait in neetcode solution it used a changing while condition
            i thought that was bad practice no?
            """
            if window_size - highest_freq > k:
                freq_map[s[L]] -= 1
                L += 1

            # dynamically max of longest str
            longest_str = max(R-L+1 , longest_str)

        return longest_str


            
                