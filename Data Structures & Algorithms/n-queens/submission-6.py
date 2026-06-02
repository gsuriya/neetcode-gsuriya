class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """

        go row by row and add to every possible row

        """

        res = []

        # mark taken cols and diags
        cols = set()
        pos_diags = set()
        neg_diags = set()

        def dfs(r, path):
            if r == n:
                res.append([''.join(row) for row in path])
                return
            
            # add queen to every spot on the row
            for c in range(n):
                # can't place at this coord so continue
                if c in cols or r+c in pos_diags or r-c in neg_diags:
                    continue

                path[r][c] = "Q"
                cols.add(c)
                pos_diags.add(r+c)
                neg_diags.add(r-c)

                dfs(r+1, path)

                # backtrack
                path[r][c] = "."
                cols.remove(c)
                pos_diags.remove(r+c)
                neg_diags.remove(r-c)
        
        dfs(0, [["."] * n for _ in range(n)])
        return res


