class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """

        generate all combos, check if valid

        """

        # generate all valid combos
        res = []
        def dfs(path, steps):
            # path building done
            s = ''.join(path)
            if len(s) == n*2:
                # check if valid
                if self.valid_parens(s):
                    res.append(s)
                return
            
            possibilities = ["))", "((", "()", ")("]
            for s in possibilities:
                path.append(s)
                dfs(path, steps-1)
                path.pop()
        
        dfs([], n)
        return res


    
    def valid_parens(self, s):
        stack = []

        for c in s:
            # opening
            if c == "(":
                stack.append(c)
            
            # closing
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False

        return True

