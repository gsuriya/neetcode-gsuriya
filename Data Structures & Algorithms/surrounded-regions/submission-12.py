class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, group):
            # base case
            if (r < 0 or r >= rows or c < 0 or c >= cols):
                return False  # we went out of bounds → touched border
            if board[r][c] == 'X' or (r, c) in visited:
                return True  # this direction is safely bounded

            visited.add((r, c))
            group.append((r, c))

            # if we're on the border, this group is NOT surrounded
            is_surrounded = True
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                is_surrounded = False

            # explore neighbors
            down = dfs(r + 1, c, group)
            up = dfs(r - 1, c, group)
            right = dfs(r, c + 1, group)
            left = dfs(r, c - 1, group)

            # if any direction leads to not-surrounded, entire group is not
            return is_surrounded and down and up and right and left

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    group = []
                    surrounded = dfs(r, c, group)
                    if surrounded:
                        for x, y in group:
                            board[x][y] = 'X'