class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        
        max_length = max_freq + k

        k = 2
        
        L         R    
        X X X Y Y Y

        map = {
            X: 3
            Y: 3
        }
        
        """

        window = defaultdict(int)
        L = 0
        max_length = 0
        maxf = 0

        for R in range(len(s)):
            # expand
            window[s[R]] += 1
            maxf = max(maxf, window[s[R]])

            # shrink
            while R-L+1 - maxf > k:
                window[s[L]] -= 1 
                if not window[s[L]]: del window[s[L]]
                L += 1
                
            # update
            max_length = max(max_length, R-L+1)

        return max_length


