class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set) # row num --> set w/ nums in that row
        col_map = defaultdict(set) # col num --> set w/ nums in that col
        square_map = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                
                if (board[i][j] in row_map[i] or board[i][j] in col_map[j] or board[i][j] in square_map[(i//3,j//3)]):
                    return False
                row_map[i].add(board[i][j])
                col_map[j].add(board[i][j])
                square_map[(i//3,j//3)].add(board[i][j])

        return True



                


