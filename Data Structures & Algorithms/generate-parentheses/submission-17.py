class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """

        generate valid combos as u dfs,
        no need to check if valid at end cus generated as valid

        add open
        - if open < n

        add close
        - if close < open


        basically:
        - js keep adding openings until ur at the limit
        - conditionally add closings if we know theres an open alr to match it

        """

        res = []

        # generates valid combos and adds to res
        def dfs(path, open, close):
            if len(path) == n*2:
                res.append(''.join(path))
                return
            
            # add opening
            if open < n:
                path.append("(")
                dfs(path, open+1, close)
                path.pop()
            
            # add closing
            if close < open:
                path.append(")")
                dfs(path, open, close+1)
                path.pop()
        
        dfs([], 0, 0)
        return res
