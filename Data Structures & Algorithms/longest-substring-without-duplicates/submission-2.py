class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}  # char --> index
        L = 0
        longest_str = 0

        for R in range(len(s)):
            if s[R] in window:
                L = max(L, window[s[R]] + 1)

            window[s[R]] = R
            longest_str = max(longest_str, R - L + 1)

        return longest_str