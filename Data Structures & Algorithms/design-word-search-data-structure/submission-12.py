class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        # insert word into trie
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        
    """

    dictionary = ["dog"]


                 i
    searchWord(" d . g ")


    from one node if u go down MULTIPLE paths
    - need to congregate those into 1 return val

    from one nodde if u go down ONE path
    - j return that 1 val from that dfs down that path

    """

    def search(self, word: str) -> bool:
        # search for word, if ., then dfs all children
        def dfs(i, curr):
            if i == len(word):
                return curr.word

            if word[i] == ".":
                # dfs all children
                for child in curr.children.values():
                    if dfs(i+1, child):
                        return True
                return False
            else:
                # j go to known child
                if word[i] not in curr.children:
                    return False
                return dfs(i+1, curr.children[word[i]])

        return dfs(0, self.root)





