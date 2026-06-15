class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        generate all possible PARTITIONS and prune 
        early ones that AREN'T palindromes

        
                a     aa  aab
              a  ab   b
              b

        1. gen prefix, if prefix valid palindrome --> pass in suffix
        2. if i at end --> path has a palindrome only partition

        """

        res = []
        
        # generates all prefixes, passes suffix
        def dfs(i, path):
            if i == len(s): # all substrings of partition r palindromes
                res.append(path.copy())
                return
            
            # gen all prefixes
            for j in range(i, len(s)):
                prefix = s[i:j+1]

                # if prefix palindrome --> pass in suffix, else stop
                pali = True
                L, R = 0, len(prefix)-1
                while L <= R:
                    if prefix[L] != prefix[R]:
                        pali = False
                    L += 1
                    R -= 1
                
                if pali: 
                    path.append(prefix)
                    dfs(j+1, path)
                    path.pop()
                else:
                    continue

        dfs(0, [])
        return res
