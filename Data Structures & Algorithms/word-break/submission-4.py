class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """

        true if s has a partition with all words in wordDict

          i
        n e e t c o d e ""


        """
        word_set = set(wordDict)

        cache = {} # i --> valid partition found from here?
        def dfs(i):
            if i == len(s):
                return True # valid partition found

            if i in cache:
                return cache[i]

            # generate all valid prefixes
            found = False
            for j in range(i, len(s)):
                prefix = s[i:j+1]

                if prefix in word_set:
                    found = found or dfs(j+1)
            
            cache[i] = found
            return found
        
        return dfs(0)


            
            
