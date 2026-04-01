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

        think of it as like ur just releasing a monster on the dfs board
        and you'll keep dfs'ing and adding to path only if 
        board[r][c] is within the trie

        rule: dfs as long as board[r][c] in trie


        search for all possible words in board
        - bounded by dfs tree
           - if char not in tree --> return
           - if u reach curr.word == True, append word

        1. create prefix tree using words
        2. dfs through grid checking prefix tree

        """

        # add all words into trie
        trie = Trie()
        for w in words:
            trie.insert(w)

        # starting from this (r, c) find all words in grid
        visited = set()
        def dfs(r, c, curr, path):
            # out of bounds, visited, board[r][c] not in trie
            if (r == len(board) or c == len(board[r]) or
                min(r, c) < 0 or (r, c) in visited or
                board[r][c] not in curr.children):
                    return
            
            visited.add((r, c))
            path.append(board[r][c])

            # if word found
            curr = curr.children[board[r][c]]
            if curr.word:
                res.add(''.join(path))

            dfs(r+1, c, curr, path)
            dfs(r, c+1, curr, path)
            dfs(r-1, c, curr, path)
            dfs(r, c-1, curr, path)

            visited.remove((r, c))
            path.pop()
    
        """
        words = [ab, abc]

        grid =  ab
                cd

        trie:
            root 
            a 
            b curr
            c


        """

        # dfs on each grid location
        res = set() # can make a word in multiple ways in grid
        for r in range(len(board)):
            for c in range(len(board[r])):
                dfs(r, c, trie.root, [])

        return list(res)










    
