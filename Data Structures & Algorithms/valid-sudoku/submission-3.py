class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # row num --> set
        cols = defaultdict(set) # col num --> set
        squares = defaultdict(set) # square coords --> set

        for i in range(len(board)):
            for j in range(len(board[i])):
                # if space blank, continue
                if board[i][j] == ".":
                    continue
                
                # add space to board, check if not alr in set
                if (board[i][j] in rows[i] 
                    or board[i][j] in cols[j]
                    or board[i][j] in squares[(i//3,j//3)]):
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[(i//3,j//3)].add(board[i][j])
        return True