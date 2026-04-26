class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """

        multi-source dfs starting from treasure chests
        -1 are blockers

        1. put treasure chests (0s) into q
        2. start multi-source bfs

        """

        # put treasure chests into q
        q = deque()
        level = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        # start multi-source bfs
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                # update coord w/ level
                grid[r][c] = level

                # add neighbors - out of bounds, visited, is a -1
                dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for dr, dc in dirs:
                    if (r+dr == len(grid) or c+dc == len(grid[r]) or 
                        min(r+dr, c+dc) < 0 or (r+dr, c+dc) in visited or
                        grid[r+dr][c+dc] == -1):
                        continue
                    
                    q.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))

            level += 1

        return

