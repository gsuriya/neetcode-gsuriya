class Solution:
    def hammingWeight(self, n: int) -> int:
        # O(# of 1 bits) --> O(1)
        # slightly more efficient w/ this trick

        count = 0
        while n > 0:
            n = n & (n-1)
            count += 1
        return count