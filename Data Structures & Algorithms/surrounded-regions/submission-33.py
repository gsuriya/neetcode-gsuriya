class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """

        1. iterate over: dfs from the edges
        - mark any Os as "keep"

        2. iterate over: not "keep" mark as X

        """
        keep = set()

        # marks edge Os and adjacents as "keep"
        def dfs(r, c):
            # out of bounds, visited, X
            if (r == len(board) or c == len(board[r]) or
                min(r, c) < 0 or (r, c) in keep or 
                board[r][c] == "X"):
                return

            keep.add((r, c))

            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
        
        # dfs from edges
        for r in range(len(board)):
            for c in range(len(board[r])):
                # edges
                if (r == 0 or r == len(board)-1 
                or c == 0 or c == len(board[r])-1):
                    dfs(r, c)

        # mark everything not "keep" as X
        for r in range(len(board)):
            for c in range(len(board[r])):
                if (r, c) not in keep and board[r][c] == "O":
                    board[r][c] = "X"

        return
        
