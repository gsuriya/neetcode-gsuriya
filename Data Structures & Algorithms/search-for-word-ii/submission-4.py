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

        1. create PrefixTree w/ words given
        2. for each cell, keep dfs'ing as long as path in tree
           - curr is your word_i
           - if curr.word = True, res.append(path)
    

        """

        # create trie and insert all words into it
        trie = Trie()
        for w in words:
            trie.insert(w)

        # dfs to add all words found from (r, c)
        visited = set()
        def dfs(r, c, curr, path):
            # if its a word
            if curr.word:
                res.add(''.join(path))

            # out of bounds, visited, (r,c) not in trie
            if (r == len(board) or c == len(board[r]) or
                min(r, c) < 0 or (r, c) in visited or 
                board[r][c] not in curr.children):
                return
            
            visited.add((r, c))
            path.append(board[r][c])

            dfs(r+1, c, curr.children[board[r][c]], path)
            dfs(r, c+1, curr.children[board[r][c]], path)
            dfs(r-1, c, curr.children[board[r][c]], path)
            dfs(r, c-1, curr.children[board[r][c]], path)

            path.pop()
            visited.remove((r, c))

        res = set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                dfs(r, c, trie.root, [])
        
        return list(res)

            


