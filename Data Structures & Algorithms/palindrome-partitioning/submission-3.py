class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """

         - dfs: generates all possible partitions
         - check if palindrome. if it IS, then pass w/ j+1 as i
        
        """
        ans = [] 

        def dfs(i, path):
            if path and not self.isPalindrome(path[-1]):
                return

            if i == len(s):
                ans.append(path.copy())            
            
            # gen prefix, pass suffix
            for j in range(i, len(s)):
                path.append(s[i:j+1])
                dfs(j+1, path)
                path.pop()

        dfs(0, [])
        return ans

    def isPalindrome(self, s):
        # two pointer approach
        L, R = 0, len(s)-1

        while L <= R:
            if s[L] != s[R]:
                return False
            
            L += 1
            R -= 1
        
        return True

