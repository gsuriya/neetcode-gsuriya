class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if len(t) > len(s) or t == "":
            return ""

        # create t_freq_map
        t_freq_map = defaultdict(int)
        for c in t:
            t_freq_map[c] += 1

        # sliding window algo
        L = 0
        window_freq_map = defaultdict(int)
        shortest_str_length = float('inf')
        substring = [0, 0]
        matches, need = 0, len(t_freq_map)

        for R in range(len(s)):
            # expand window, update matches
            window_freq_map[s[R]] += 1
            if s[R] in t_freq_map and window_freq_map[s[R]] == t_freq_map[s[R]]: # adding resulted in equal
                matches += 1

            # shrink window, update matches
            while matches == need:
                # update res INSIDE shrink b/c after WC is false
                temp = shortest_str_length
                shortest_str_length = min(R-L+1, shortest_str_length)
                if temp != shortest_str_length: # act smaller substring found
                    substring[0], substring[1] = L, R

                if s[L] in t_freq_map and window_freq_map[s[L]] == t_freq_map[s[L]]: # equal rn, about to decrement causing mismatch
                    matches -= 1
                window_freq_map[s[L]] -= 1
                L += 1

        # return substring w/ final indices
        return s[substring[0] : substring[1]+1] if shortest_str_length != float('inf') else ""



        