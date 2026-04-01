class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                
                # add to rows
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])
                
                # add to cols
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])

                # add to boxes
                if board[i][j] in boxes[(i//3,j//3)]:
                    return False
                boxes[(i//3, j//3)].add(board[i][j])
        
        return True