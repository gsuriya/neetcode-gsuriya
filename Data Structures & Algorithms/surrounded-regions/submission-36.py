class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        
        the only way u don't get turned into an X is if u 
        hv a block connection to the border

        Os on edges and any block connections to them r SAFE
        - everything else is an X

        steps:
        1. dfs on all border Os
        - add them and their blocks to "safe"
        2. make everything X excluding "safe"

        """
        # adds Os to "safe"
        def dfs(r, c, visited):
            # out of bounds, visited, is an X
            if (r == len(board) or c == len(board[r]) or
                min(r, c) < 0 or (r, c) in visited or 
                board[r][c] == "X"):
                return
            
            visited.add((r, c))

            dfs(r+1, c, visited)
            dfs(r-1, c, visited)
            dfs(r, c+1, visited)
            dfs(r, c-1, visited)

        # dfs all border 0s - them + blocks to "safe"
        safe = set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                if (r == 0 or c == 0 or r == len(board)-1 or
                    c == len(board[r])-1):
                    dfs(r, c, safe)

        # make everything X excluding "safe"
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X"
        
        return
        

