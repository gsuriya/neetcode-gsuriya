class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """

        multi source bfs
        1. put 0s into queue initially
        2. bfs
        - can't go to -1s, replace infs
        - visited

        """

        # put 0s in to queue initially
        q = deque()
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        # bfs
        level = 0
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = level

                # append valid neighbors
                dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for dr, dc in dirs:
                    # out of bounds, visited, is a -1
                    if (r+dr == len(grid) or c+dc == len(grid[r+dr]) or
                        min(r+dr, c+dc) < 0 or (r+dr, c+dc) in visited or
                        grid[r+dr][c+dc] == -1):
                        continue
                    
                    q.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))
            
            level += 1

        return
        




