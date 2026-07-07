class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """

        row_map # r number --> nums in that row
        same for cols and squares

        """
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        square_map = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in row_map[r] or 
                    board[r][c] in col_map[c] or
                    board[r][c] in square_map[(r//3, c//3)]):
                    return False
                
                row_map[r].add(board[r][c])
                col_map[c].add(board[r][c])
                square_map[(r//3, c//3)].add(board[r][c])
        
        return True