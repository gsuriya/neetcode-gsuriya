class Solution:
    def numDecodings(self, s: str) -> int:
        """
        O(1) space, O(N) time

            i  
        1 0 1 2 ""
    dp  4 0 2 1 1 

        if prefix is valid:
            dp[i] = sum all # of partitions for all possible suffixes
        else:
            dp[i] = 0

        """

        dp = [0 if s[-1] == "0" else 1, 1]

        for i in range(len(s)-2, -1, -1):
            if s[i] == "0":
                tmp = dp[0]
                dp[0] = 0
                dp[1] = tmp
                continue

            tmp = dp[0]
            dp[0] = dp[0] + dp[1] if int(s[i:i+2]) <= 26 else dp[0]
            dp[1] = tmp 
        
        return dp[0]

        
