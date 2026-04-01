class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row, col, square # --> set
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        square_map = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue

                # if in map, return False, else add
                if board[i][j] in row_map[i] or board[i][j] in col_map[j] or board[i][j] in square_map[(i//3,j//3)]:
                    return False
                row_map[i].add(board[i][j])
                col_map[j].add(board[i][j])
                square_map[(i//3,j//3)].add(board[i][j])
        
        return True