class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """

        if prefix in word --> continue else prune
        
        once valid partition reached --> bubble up true

        """
        word_set = set(wordDict)

        # returns if valid partition can be reached from here
        cache = {} # i --> possible to reach valid partition from here
        def dfs(i):
            if i in cache:
                return cache[i]

            if i == len(s): 
                return True
            
            # generate partitions
            valid = False
            for j in range(i, len(s)):
                prefix = s[i:j+1]
                
                if prefix in word_set:
                    valid = valid or dfs(j+1)
            
            cache[i] = valid
            return valid
        
        return dfs(0)
