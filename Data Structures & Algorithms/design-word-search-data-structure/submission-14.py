class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        # insert into Trie
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        # dfs search: if "." search all children

        def dfs(i, curr):
            if i == len(word):
                return curr.word
            
            c = word[i]
            if c == ".":
                for child in curr.children.values():
                    if dfs(i+1, child):
                        return True
                return False
            
            else: # j move to c in trie
                if c not in curr.children:
                    return False
                return dfs(i+1, curr.children[c])
        
        return dfs(0, self.root)






