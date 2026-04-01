class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """

        multi-source bfs starting from the treasure chests

        1. add all treasure chests into the q

        2. start bfs --> replace each grid cell w/ current level


        """

        # append all 0s to q
        q = deque()
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        # start bfs
        
        level = 0
        while q:
            for _ in range(len(q)): # so level layer by layer
                r, c = q.popleft()

                grid[r][c] = level # update w/ distance

                # append children - check if valid before appending to q
                neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in neighbors:
                    # out of bounds, visited, is a -1
                    if (r+dr == len(grid) or c+dc == len(grid[r+dr]) or
                        min(r+dr, c+dc) < 0 or ((r+dr, c+dc) in visited or
                        grid[r+dr][c+dc] == -1)):
                        continue
                    q.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))

            level += 1



