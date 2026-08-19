class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """

        check in row, col, and square

        row num --> set(nums in that row)
        col num --> set(col nums in that row)
        square num --> set(square nums in that row)

        for every num
        - check if that num alr exists in either the row, col, or square

        """

        # dicts
        row_map = defaultdict(set) # row number --> set
        col_map = defaultdict(set)
        square_map = defaultdict(set) # (r//3, c//3)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                
                # check if this num is alr in a row, col, or square
                if (board[r][c] in row_map[r] or 
                    board[r][c] in col_map[c] or 
                    board[r][c] in square_map[(r//3, c//3)]):
                    return False
                
                row_map[r].add(board[r][c])
                col_map[c].add(board[r][c])
                square_map[(r//3, c//3)].add(board[r][c])

        
        return True


