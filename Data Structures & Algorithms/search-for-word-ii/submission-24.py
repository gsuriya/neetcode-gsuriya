class TrieNode:
    def __init__(self):
        self.children = {} # char --> node representing that char
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

        1. create trie of words
        2. dfs on board constrained by trie

        """

        trie = Trie()
        for w in words:
            trie.insert(w)

        res = set()

        # dfs should be appending words
        def dfs(r, c, curr, visited, path):
            # out of bounds, visited, not in trie
            if (r == len(board) or c == len(board[r]) or 
                min(r, c) < 0 or (r, c) in visited or 
                board[r][c] not in curr.children):
                return

            visited.add((r, c))
            path.append(board[r][c])

            # move to this letter in Trie
            curr = curr.children[board[r][c]]
            if curr.word: # word found
                res.add(''.join(path))

            dfs(r+1, c, curr, visited, path)
            dfs(r, c+1, curr, visited, path)
            dfs(r-1, c, curr, visited, path)
            dfs(r, c-1, curr, visited, path)

            path.pop()
            visited.remove((r, c))

        
        for r in range(len(board)):
            for c in range(len(board[r])):
                dfs(r, c, trie.root, set(), [])
        
        return list(res)



















