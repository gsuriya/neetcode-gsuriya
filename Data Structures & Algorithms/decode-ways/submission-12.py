class Solution:
    def numDecodings(self, s: str) -> int:
        """
        cut / ~cut --> 2 options for each letter, append path to res
        O(n * 2^n)
        in palindrome partitioning, had to gen partitions so HAD to 
        use this algo
        in this problem, it js wants NUMBER of ways so prolly DP pattern
        ord(c)-ord('A')


        METHOD 1: generate valid partitions algo
        - prune if theres a leading zero

        1012


        """
        
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i == len(s):
                return 1
            
            # generate all prefixes, if leading 0 then don't recurse
            count = 0
            for j in range(i, len(s)):
                prefix = s[i:j+1]
                if prefix[0] == "0" or int(prefix) > 26:
                    continue
                
                count += dfs(j+1)
            
            cache[i] = count
            return count
        
        return dfs(0)
            

                
                
                





