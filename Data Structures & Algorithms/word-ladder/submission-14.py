class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """

        bfs but NOW 
        positionally off by one wildcard matching

        undirected graph

                    cat
                     |
                    bat
                     |
                    bag
                   /   \
                dag --- sag

        """

        # build pattern_map from list of words
        pattern_map = defaultdict(list)
        for word in wordList:
            # gen patterns
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)

        # bfs, check neighbors by using pattern_map
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
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for w in pattern_map[pattern]:
                        if w in visited:
                            continue
                        
                        q.append(w)
                        visited.add(w)

            level += 1
        
        return 0 # endWord never found b/c level never returned earlier







