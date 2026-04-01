class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """

        dfs on every word[0] in board

        word_index has to match as we keep recursing

        """        

        # recurse max 3 spaces to find word, word_i matching
        visited = set()

        def dfs(r, c, word_i):
            # i ends up going to end --> word found
            if word_i == len(word):
                return True
    
            # out of bounds, visited, word_i != curr letter
            if (min(r, c) < 0 or r == len(board) or c == len(board[r]) or
                (r, c) in visited or word[word_i] != board[r][c]):
                return False
            
            visited.add((r, c))

            word_found = (
                dfs(r+1, c, word_i+1) or
                dfs(r, c+1, word_i+1) or
                dfs(r-1, c, word_i+1) or
                dfs(r, c-1, word_i+1)
            )
            
            visited.remove((r, c)) # try all possible combinations
            
            return word_found


        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True # if at least one has word
        
        return False



