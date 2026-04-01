class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """

        for m cell, dfs 4 directions len(word) times

        """

        visited = set()
        def dfs(r, c, word_i):
            # word found - if word_i able to pass to the end
            if word_i == len(word):
                return True

            # base cases - out of bounds, incorrect letter, visited
            if (min(r, c) < 0 or r == len(board) or c == len(board[0]) or
               word[word_i] != board[r][c] or (r,c) in visited):
               return False

            visited.add((r,c))

            # word found from this cell
            word_found = (dfs(r+1, c, word_i+1) or
                         dfs(r-1, c, word_i+1) or
                         dfs(r, c+1, word_i+1) or
                         dfs(r, c-1, word_i+1))

            visited.remove((r,c))      

            # 'or' assumes False until proven True --> True bubbles up
            return word_found      

        
        for r in range(len(board)):
            for c in range(len(board[r])):
                # if at least one of the starting squares makes a path with the word then return True
                if dfs(r, c, 0):
                    return True

        # no words found after we dfs'd from every starting location, so return False
        return False