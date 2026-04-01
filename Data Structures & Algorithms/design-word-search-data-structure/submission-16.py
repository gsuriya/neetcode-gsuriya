"""

words = ["day", "bay", "may", "say"]

trie:
            root
        d    b    m    s
        a    a    a    a
        y    y    y    y


searchWord(".ay") --> True

option 1: brute force
- O(N * M) where N is #words and M is #letteres for searchword

option 2: hashmap

map # pattern --> words w/ that pattern
{
    .ay : ["day"]
    d.y : ["day"]
    da. : ["day"]

   space:  O(2^len(word) * N)
   time: O(1)
}


option 3: trie
- 1. insert all the words into a trie
- 2. if "." dfs all children, if not, then j go to that child


"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    # inserting into trie
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children: 
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        
    # searching in the trie (modified for ".")
    def search(self, word: str) -> bool:

        def dfs(i, curr):
            # base case: i reached the end
            if i == len(word): 
                return curr.word
            
            if word[i] == ".":
                # dfs all children, return True if any of them r true
                for child in curr.children.values():
                    if dfs(i+1, child):
                        return True
                return False
            
            else:
                # j go to child in trie if its there
                if word[i] not in curr.children:
                    return False
                return dfs(i+1, curr.children[word[i]])
        
        return dfs(0, self.root)





        
 