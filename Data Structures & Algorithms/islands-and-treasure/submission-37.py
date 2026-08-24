class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """

        multi-source bfs

        1. put all treasure chests into q
        2. bfs - set (r, c) coord to level

        """

        # put treasure chests into q
        visited = set()
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))
        
        # bfs - set popped coords to level
        level = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = level

                # add neighbors
                dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for dr, dc in dirs:
                    # out of bounds, visited, is a -1
                    if (r+dr == len(grid) or c+dc == len(grid[r]) or
                        min(r+dr, c+dc) < 0 or (r+dr, c+dc) in visited or
                        grid[r+dr][c+dc] == -1):
                        continue
                    
                    visited.add((r+dr, c+dc))
                    q.append((r+dr, c+dc))
                
            level += 1
        
        return



