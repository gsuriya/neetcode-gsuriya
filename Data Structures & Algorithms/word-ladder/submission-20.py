class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """

        "cat" --> "sag"

        UNDIRECTED GRAPH
                cat
                 |
                bat
                 |
                bag
                /  \
             sag -- dag

        da js do bfs from start node to end node, return min distance (level)

        1. do normally O(N * N * L)
        2. off-by-one pattern matching O(N * L)

        "cat"

        pattern_map = {
            *at = [cat, bat]
            c*t = [cat]
            ca* = [cat]
            *ag = [bag, sag, dag]
        }

          i
        c a t

        """
        # create pattern_map using wordList to find valid neighbors later
        pattern_map = defaultdict(list) # pattern --> [words w/ this pattern]
        for w in wordList:
            for i in range(len(w)):
                p = w[:i] + "*" + w[i+1:]
                pattern_map[p].append(w)

        q = deque([beginWord])
        level = 0
        visited = set(beginWord)

        while q:
            for _ in range(len(q)):
                w = q.popleft()

                if w == endWord: 
                    return level+1 

                # append valid neighbors - generate patterns for curr word
                for i in range(len(w)):
                    p = w[:i] + "*" + w[i+1:]
                    
                    for nei in pattern_map[p]:
                        if nei in visited:
                            continue
                        q.append(nei)
                        visited.add(nei)

            level += 1
        
        return 0 # if no sequence exists
