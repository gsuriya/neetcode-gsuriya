class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """

        add each coord to row, col, square sets
        - if duplicate in any of those sets before u add, return false

        return true at end

        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                
                # check duplicates
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3,c//3)]):
                    return False

                # add to sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        
        return True



