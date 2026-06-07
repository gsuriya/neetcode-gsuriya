class Solution:
    def countBits(self, n: int) -> List[int]:
        """

        0 - 0000
        1 - 0001
        2 - 0010
        3 - 0011
        
        any binary number:
        prefix + LSB

        dp = # of bits in the prefix

        001 1

        dp = [0, 1]

        """

        dp = [0] * (n+1) # i for dp is the number of 1-bits for i itself
        dp[0] = 0 # number of 1-bits for 0 is 0

        for i in range(n+1):
            prefix_1s = dp[i >> 1] # get number of 1-bits of prefix
            LSB = i & 1 # is LSB a 1 or a 0
            
            dp[i] = prefix_1s + LSB
        
        return dp