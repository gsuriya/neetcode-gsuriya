class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r, c, word_index, visited):
            # base cases
            # out of bounds, visited, incorrect letter
            if word_index == len(word):
                return True
            
            if (r < 0 or c < 0 or r == len(board) or c == len(board[0]) or
               (r,c) in visited
                or word[word_index] != board[r][c]):
                return False

            visited.add((r, c))

            contains_word = (dfs(r+1, c, word_index + 1, visited) or
                            dfs(r-1, c, word_index + 1, visited) or
                            dfs(r, c+1, word_index + 1, visited) or
                            dfs(r, c-1, word_index + 1, visited))

            visited.remove((r, c))

            return contains_word
            
        
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if dfs(r, c, 0, set()):
                    return True
        
        return False
