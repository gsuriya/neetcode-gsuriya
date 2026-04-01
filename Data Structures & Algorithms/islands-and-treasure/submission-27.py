class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """

        multi-source dfs 

        1. put treasure chests in q initially
        2. start bfs
        - replace each curr coord w/ level
        - -1 cannot be traversed


        """

        # enqueue all treasure chests
        q = deque()
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        # start multi-source bfs
        level = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = level

                # enqueue valid children
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for dr, dc in directions:
                    # out of bounds, visited, is a -1
                    if (r+dr == len(grid) or c+dc == len(grid[r]) or
                        min(r+dr, c+dc) < 0 or (r+dr, c+dc) in visited or
                        grid[r+dr][c+dc] == -1):
                        continue
                    
                    q.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))

            level += 1

        return None # modify grid in place





