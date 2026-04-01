class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set) # row num --> set for that row
        col_map = defaultdict(set) # col num --> set for that col
        square_map = defaultdict(set) # square coord --> set for that square

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                
                # check for duplicates in the set
                # if in set, return False, else add it
                if board[i][j] in row_map[i] or board[i][j] in col_map[j] or board[i][j] in square_map[(i//3,j//3)]:
                    return False
                row_map[i].add(board[i][j])
                col_map[j].add(board[i][j])
                square_map[(i//3,j//3)].add(board[i][j])

        return True 
