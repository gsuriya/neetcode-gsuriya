class Solution:
    def countBits(self, n: int) -> List[int]:
        """

        sets of 4 numbers use (0-3 pattern for # of 1s)

        these set of 4 numbers have their own number binary bits, and then you add amount for 4 and shit too

        """

        bits = [0] * (n + 1)

        for i in range(1, n + 1):
            bits[i] = bits[i >> 1] + (i & 1)

        return bits