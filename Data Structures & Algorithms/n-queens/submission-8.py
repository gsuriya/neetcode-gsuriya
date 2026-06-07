class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # taken coords
        cols = set()
        pos_diags = set()
        neg_diags = set() 

        # place queen in every col in the row
        res = []
        def dfs(r, path):
            if r == n:
                res.append([''.join(row) for row in path])
                return
            
            for c in range(n):
                # can't place a queen here
                if c in cols or r+c in pos_diags or r-c in neg_diags:
                    continue

                # place queen and backtrack for next placement
                path[r][c] = "Q"
                cols.add(c)
                pos_diags.add(r+c)
                neg_diags.add(r-c)

                dfs(r+1, path)
                
                path[r][c] = "."
                cols.remove(c)
                pos_diags.remove(r+c)
                neg_diags.remove(r-c)

        dfs(0, [["."] * n for _ in range(n)])
        return res


