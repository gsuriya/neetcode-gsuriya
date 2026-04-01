class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {} # char --> node that points to that location

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:

        def dfs(i, curr):
            # word found
            if i == len(word) and curr.word == True:
                return True
            
            if i < len(word) and word[i] == ".":
                # dfs all children
                for child in curr.children.values():
                    if dfs(i+1, child):
                        return True
                return False # if all the iterations found nothing
            elif i < len(word) and word[i] != ".":
                # j go to the path we need
                if word[i] not in curr.children:
                    return False
                return dfs(i+1, curr.children[word[i]])
            
            return False
        
        return dfs(0, self.root)







        
