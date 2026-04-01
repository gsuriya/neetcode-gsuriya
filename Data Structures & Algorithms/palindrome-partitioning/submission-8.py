class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        think of this more like iteration w/ i pointer rather than prefix passing in suffix
        the i pointer

        goal: generate all partitions, res.append() ones that r palindromes

        base case
        - if i reaches end, means everything before valid prefixes

        gen prefixes
        - if prefix valid palindrome, pass in suffix
        

        """

         # uses global var s
        def is_pali(L, R):
            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True


        res = []

        def dfs(i, path):
            # i reaches the end
            if i == len(s):
                res.append(path.copy())
                return
            
            # generate prefixes
            for j in range(i, len(s)):
                # u aren't passing in prefix, ur passing in SUFFIX
                # so u need to check if prefix is_pali RIGHT NOW
                if is_pali(i, j):
                    path.append(s[i:j+1])
                    dfs(j+1, path) # prefix is palindrome so now pass in suffix
                    # u pass in suffix by j passing in next index i
                    path.pop()
        
        dfs(0, [])
        return res


       
