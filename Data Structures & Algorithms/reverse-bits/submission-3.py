class Solution:
    def reverseBits(self, n: int) -> int:
        """

        given 32-bit n so iterating through 
        all bits O(1) time and space

        repeat until n is 0 and everything chopped off
        1. extract rightmost bit from n (& 1)
        2. chop off rightmost bit from n
        3. append rightmost bit to res


        """

        res = 0
        for _ in range(32):
            bit = n & 1 # %2
            n >>= 1 # //2

            res = (res << 1) | bit

        return res
            




