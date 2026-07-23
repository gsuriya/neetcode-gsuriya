class Solution:
    def numDecodings(self, s: str) -> int:
        """


        i
        1 0 1 2 ""
dp      

        """

        cache = {} # i --> num ways to partition
        def dfs(i):
            if i == len(s):
                return 1 # valid partition found
            
            if i in cache:
                return cache[i]
            
            # generate valid prefixes
            count = 0
            for j in range(i, len(s)):
                prefix = s[i:j+1]

                if prefix[0] != "0" and int(prefix) <= 26:
                    count += dfs(j+1)
            
            cache[i] = count
            return count
        
        return dfs(0)

