class Solution:
    def numDecodings(self, s: str) -> int:
        """

              i  
        1 0 1 2 ""
    dp  0 0 0 0 1 

        i  
        0 6 ""
    dp  0 1 1 

        """

        dp = [0] * (len(s)+1)
        dp[-1] = 1

        for i in range(len(s)-1, -1, -1):
            if int(s[i]) == 0:
                dp[i] = 0
                continue

            count = 0
            for j in range(i, len(s)):
                prefix = s[i:j+1]

                if int(prefix) <= 26:
                    count += dp[j+1] # now u can add num of partitions from this point

            dp[i] = count
        
        return dp[0]



        


        