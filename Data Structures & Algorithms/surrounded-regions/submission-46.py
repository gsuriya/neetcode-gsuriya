class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """

        - border Os can NEVER be captured
        - border Os that CONNECT TO inner Os 
            --> whole region can't be captured

        1. dfs from border Os --> mark all as safe
        2. iterate thru board turn rest of Os to Xs

        """

        # dfs from border Os --> mark as "safe" using visited set
        def dfs(r, c, visited):
            # out of bounds, visited
            if (r == len(board) or c == len(board[r]) or min(r, c) < 0 or
                (r, c) in visited or board[r][c] != "O"):
                return
            
            visited.add((r, c))

            dfs(r+1, c, visited)
            dfs(r-1, c, visited)
            dfs(r, c+1, visited)
            dfs(r, c-1, visited)
        
        # mark all border O regions as safe
        safe = set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                # border O
                if (r == 0 or c == 0 or r == len(board)-1 
                or c == len(board[r])-1):
                    if board[r][c] == "O":
                        dfs(r, c, safe)
            
        # turn everything but safe into X
        for r in range(len(board)):
            for c in range(len(board[r])):
                if (r, c) not in safe and board[r][c] == "O":
                    board[r][c] = "X"
        
        return
        