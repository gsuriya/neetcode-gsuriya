class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # row num --> numbers in that row
        cols = defaultdict(set) # col num --> numbers in that col
        squares = defaultdict(set) # (r//3, c//3) --> numbers in that square

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue

                # check if duplicates
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                # if no dups, then add to sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        return True
                

