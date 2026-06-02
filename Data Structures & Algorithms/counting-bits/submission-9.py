class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        
        # of 1s = # of 1s in prefix + LSB (1 or 0)

        n = 4

             
        dp = [0, 1, 1, 2, 1]
        n     0  1  2  3  4

        3 --> 11

        take # of 1-bits of the prefix (1) --> 1 1-bit
        then add on the LSB (11 & 1 = 1) --> += 1 1-bit
                                            ----------
                                                2 1-bits


        arbitrary number: 1010101101101
                          # of 1-bits(101010110110) + LSB 0 or 1 (1)
                          - derived from dp arr      - derived by n & 1
                          - n // 2

        """

        dp = [0] *(n+1) # 0-n means n+1 cells
        dp[0] = 0 # number of 1-bits for 0 is 0, this is the dp val we will use

        for i in range(1, len(dp)):
            # get num of 1-bits in prefix of i
            prefix_1s = dp[i >> 1]
            LSB = i & 1

            dp[i] = prefix_1s + LSB
        
        return dp



