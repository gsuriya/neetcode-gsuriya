class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """

        rotten --> fresh fruit

        1. add rotten fruit to q, count how many fresh fruit
        2. multi-source dfs
        - if fresh fruit still there, return -1

        """

        # add rotten fruit to q, count fresh fruit
        q = deque()
        level = 0
        visited = set()

        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2: # rotten
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1: # fresh
                    fresh += 1
        
        if not fresh:
            return 0

        # multi-source bfs (2 --> 1)
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                # keep track of fresh fruit left after dfs
                if grid[r][c] == 1:
                    fresh -= 1
                grid[r][c] = 2

                # add neighbors - out of bounds, visited, not a fresh fruit
                dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for dr, dc in dirs:
                    if (r+dr == len(grid) or c+dc == len(grid[r]) or
                        min(r+dr, c+dc) < 0 or (r+dr, c+dc) in visited or
                        grid[r+dr][c+dc] != 1):
                        continue
                    
                    q.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))
            
            level += 1
        
        if fresh:
            return -1
        
        return level-1





