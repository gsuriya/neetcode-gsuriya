class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # empty_set

        # for num in iterable:
            # if num in empty_set: --> duplicate
            # empty_set.add(num)

        row_map = defaultdict(set)
        col_map = defaultdict(set)
        square_map = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue

                # check if row valid
                if board[i][j] in row_map[i]:
                    return False
                row_map[i].add(board[i][j])
                
                # check if col valid
                if board[i][j] in col_map[j]:
                    return False
                col_map[j].add(board[i][j])

                # check if square valid
                if board[i][j] in square_map[(i//3,j//3)]:
                    return False
                square_map[(i//3,j//3)].add(board[i][j])
        
        return True