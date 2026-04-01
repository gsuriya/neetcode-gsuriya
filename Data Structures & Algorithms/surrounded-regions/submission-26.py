class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        i initially thought check for O group surrounded by Xs --> ran into a wall

        Q: What is the criteria for a group to be "surrounded"?
        - surrounded by Xs
        
        Q: What is the criteria for a group to be NOT "surrounded"?
        - HAVE >= 1 O ON THE BORDER
        - EUREKA

        1. dfs on edges, mark unsurrounded O groups with "T"
        2. iterate through, mark all Os (surrounded) as X

        """

        # mark unsurrounded O groups as T
        def dfs(r, c, visited):
            # base cases - out of bounds, visited, no "X"
            if (min(r, c) < 0 or r == len(board) or c == len(board[r]) or
               (r, c) in visited or board[r][c] == "X"):
               return

            # only Os
            visited.add((r, c))
            board[r][c] = "T"

            dfs(r+1, c, visited)
            dfs(r-1, c, visited)
            dfs(r, c+1, visited)
            dfs(r, c-1, visited)
    
        # dfs at the edges --> mark unsurrounded O groups as "T"
        for r in range(len(board)):
            for c in range(len(board[r])):
                if (r == 0 or r == len(board)-1 or c == 0 or c == len(board[r])-1):
                    dfs(r, c, set())
        
        # mark rest of surrounded Os as "X"
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        

        