class Solution:
    def hammingWeight(self, n: int) -> int:
        """

        count the 1 and shift

        """

        count = 0
        while n:
            if n & 1:
                count += 1
            n >>= 1
        return count