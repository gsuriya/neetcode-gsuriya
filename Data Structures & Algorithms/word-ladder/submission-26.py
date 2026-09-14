class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """

        1. create pattern_map
        2. bfs algo to endWord
        - return level

        pattern_map = {
            *at: [bat]
            b*t: [bat]
            ba*: [bat, bag]
        }

        """

        # build pattern_map to find neighbors
        pattern_map = defaultdict(list) # pattern (*at) --> [words w/ that pattern]
        for w in wordList:
            # create every pattern for each word
            for i in range(len(w)):
                p = w[:i] + "*" + w[i+1:]
                pattern_map[p].append(w)
        
        # start dfs, return level
        q = deque([beginWord])
        visited = set(beginWord)
        level = 0

        while q:
            for _ in range(len(q)):
                w = q.popleft()

                if w == endWord:
                    return level+1
                
                # enqueue neighbors
                for i in range(len(w)):
                    p = w[:i] + "*" + w[i+1:]
                    for nei in pattern_map[p]:
                        if nei == w or nei in visited:
                            continue
                        
                        q.append(nei)
                        visited.add(nei)
                        
            level += 1

        return 0
        
        
        
