class TrieNode:
    def __init__(self):
        self.children = {} # char --> node representing that char
        self.word = False

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
            if i == len(word):
                return curr.word # return True if get to the end
            
            if word[i] == ".": # dfs all children
                for c in curr.children:
                    if dfs(i+1, curr.children[c]):
                        return True
                return False

            else: # js go to child
                if word[i] not in curr.children:
                    return False
                return dfs(i+1, curr.children[word[i]])

        return dfs(0, self.root)

                
        
