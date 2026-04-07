class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """

        if impossible to get all fresh fruit, return 0

        steps:
        1. multi-source bfs
        - add all rotten fruit (2) to q
        - valid neighbors r fresh fruit (1)

        2. iterate thru grid
        - if fresh fruit left return -1 else return level

        """

        # initially add all 2s to q
        q = deque()
        visited = set()
        fresh_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
        
        if not fresh_count:
            return 0
        
        # bfs
        level = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if grid[r][c] == 1: # count fresh --> rotten
                    fresh_count -= 1
                grid[r][c] = 2

                dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for dr, dc in dirs:
                    # out of bounds, visited, not a 1
                    if (r+dr == len(grid) or c+dc == len(grid[r]) or 
                        min(r+dr, c+dc) < 0 or (r+dr, c+dc) in visited or
                        grid[r+dr][c+dc] != 1):
                        continue
                    
                    q.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))

            level += 1
        
        return level-1 if fresh_count == 0 else -1









