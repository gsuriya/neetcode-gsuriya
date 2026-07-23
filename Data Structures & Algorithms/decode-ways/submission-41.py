class Solution:
    def numDecodings(self, s: str):
        """

             j
             i
        1 0 1 2 ""
dp              1

        """

        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            count = 0

            for j in range(i, len(s)):
                prefix = s[i:j + 1]

                if prefix[0] != "0" and int(prefix) <= 26:
                    count += dp[j + 1]

            dp[i] = count

        return dp[0]


        