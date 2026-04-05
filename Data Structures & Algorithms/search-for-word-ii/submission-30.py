class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """

        1. insert all words into a Trie

        2. dfs ALL r,c on board bounded by the Trie
        - if word found, append to res
        - u can find same word multiple ways in grid, so make res set

        """
        # insert words into trie
        trie = Trie()
        for w in words:
            trie.insert(w)
        
        # populates res, finds every word bounded by trie
        visited = set()
        def dfs(r, c, curr, path):
            # out of bounds, visited, not in trie
            if (r == len(board) or c == len(board[r]) or 
                min(r, c) < 0 or (r, c) in visited or
                board[r][c] not in curr.children):
                return
            
            visited.add((r, c))
            path.append(board[r][c])
            
            curr = curr.children[board[r][c]]
            if curr.word:
                res.add(''.join(path))

            dfs(r+1, c, curr, path)
            dfs(r-1, c, curr, path)
            dfs(r, c+1, curr, path)
            dfs(r, c-1, curr, path)

            path.pop()
            visited.remove((r, c))
            

        # dfs all r, c bounded by trie
        res = set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                dfs(r, c, trie.root, [])
        
        return list(res)

        





