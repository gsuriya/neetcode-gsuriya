class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """

        bfs instead

        undirected graph

                    cat
                     |
                    bat
                     |
                    bag
                   /   \
                dag --- sag

        """

        q = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        level = 0

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return level+1
                
                # enqueue valid transformations (neighbors)
                for w in wordList:
                    diff = 0
                    for i in range(len(w)):
                        if w[i] != word[i]:
                            diff += 1
                    valid = True if diff == 1 else False
                    
                    # visited, not valid
                    if w in visited or not valid:
                        continue
                    
                    q.append(w)
                    visited.add(w)

            level += 1

        # endWord never found b/c level never returned earlier
        return 0 


