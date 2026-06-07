class Solution:
    def reverseBits(self, n: int) -> int:
        """ 

        32-bit unsigned --> O(32) --> O(1)
        - account for ALLLL 32 bits

        pop bits from n, append to res

        000000010101


        """

        res = 0
        for _ in range(32): # pop and append 32 times
            bit = n & 1 # extract bit
            n >>= 1 # cut off bit

            res = (res << 1) + bit # append to res

        return res