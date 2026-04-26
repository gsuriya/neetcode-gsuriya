class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """

        only way for O to be NOT surrounded is if O is connected to border

        1. dfs border, if O --> then mark all connnected Os as safe
        2. turn everything else (other than safe) to X

        """
        # mark Os as safe
        safe = set()
        def dfs(r, c):
            # out of bounds, visited, not an O
            if (r == len(board) or c == len(board[r]) or min(r, c) < 0
                or (r, c) in safe or board[r][c] != "O"):
                return
            
            safe.add((r, c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # mark safe - dfs Os from border
        for r in range(len(board)):
            for c in range(len(board[r])):
                if ((r == 0 or c == 0 or r == len(board)-1 or 
                    c == len(board[r])-1) and board[r][c] == "O"):
                    dfs(r, c)

        # make everything X
        for r in range(len(board)):
            for c in range(len(board[r])):
                if (r, c) not in safe:
                    board[r][c] = "X"
        
        return



