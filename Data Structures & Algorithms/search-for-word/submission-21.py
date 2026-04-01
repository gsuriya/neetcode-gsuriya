class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """

        dfs through word and grid

        1. start dfs on every cell where starting letter matches
        - if any one of those dfs's finds the word, return True

        """

        # search for word
        visited = set()
        def dfs(r, c, i):
            # word found
            if i == len(word):
                return True
            
            # out of bounds, visited, not correct letter
            if (r == len(board) or c == len(board[r]) or min(r, c) < 0 or
                (r, c) in visited or board[r][c] != word[i]):
                return False
            
            visited.add((r, c))

            word_found = (
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1)
            )

            visited.remove((r, c))

            return word_found


        # dfs every cell
        for r in range(len(board)):
            for c in range(len(board[r])):
                if dfs(r, c, 0):
                    return True
        
        return False
        

        