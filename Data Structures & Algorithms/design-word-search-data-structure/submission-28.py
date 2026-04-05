class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    """    
                 i 
    search(d . y)

          root
            d
          c a b
          z y 
            a
    """

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # insert into trie
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:

        def dfs(i, curr):
            if i == len(word):
                return curr.word # only return True if its an act word inserted in, not just the prefix

            if word[i] == ".": # search all children
                for c in curr.children:
                    if dfs(i+1, curr.children[c]):
                        return True
                return False # if none of children returned Treu

            else: # js go to char
                if word[i] not in curr.children:
                    return False
                return dfs(i+1, curr.children[word[i]])
        
        return dfs(0, self.root)


        
