class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    
    # regular Trie insert function
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        
    """

    if . then dfs everything

      i
    d.y
                c
                d

                a s    b

                y     z

    """
    def search(self, word: str) -> bool:
        
        def dfs(i, curr):
            if i == len(word):
                return curr.word
    
            if word[i] == ".": # dfs check all children
                for c in curr.children:
                    if dfs(i+1, curr.children[c]):
                        return True
                return False

            else: # just go to it
                if word[i] not in curr.children:
                    return False
                return dfs(i+1, curr.children[word[i]])
        
        return dfs(0, self.root)







