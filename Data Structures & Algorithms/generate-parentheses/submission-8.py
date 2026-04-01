class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        n = 3

        dfs(path + '(')
        dfs(path + ')')

        """
        valid_parens = []
        def dfs(path, count_opening, count_closing):
            if len(path) == 2*n:
                valid_parens.append(path)
                return
            
            if count_opening < n:
                dfs(path + "(", count_opening+1, count_closing)
            if count_closing < count_opening:
                dfs(path + ")", count_opening, count_closing+1)

        dfs("", 0, 0)
        return valid_parens
        
        