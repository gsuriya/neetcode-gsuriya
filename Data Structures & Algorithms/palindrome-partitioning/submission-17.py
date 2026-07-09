class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """

        generate all possible partitions
        - if one of the prefixes is NOT a palindrome --> prune

                    []
                a   aa  aab
               a ab b
              b

        reaches end and partition fully created --> append to res

        """
        res = []
        def dfs(i, path):
            if i == len(s):
                res.append(path.copy())
                return
            
            # generate prefixes, pass in suffix
            for j in range(i, len(s)):
                prefix = s[i:j+1]

                if self.palindrome(prefix):
                    path.append(prefix)
                    dfs(j+1, path)
                    path.pop()

        dfs(0, [])
        return res
    
    def palindrome(self, s):
        L, R = 0, len(s)-1

        while L <= R:
            if s[L] != s[R]:
                return False
            
            L += 1
            R -= 1
        
        return True

