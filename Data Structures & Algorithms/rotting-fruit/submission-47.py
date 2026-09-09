class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """

        multi-source bfs

        1. add rotten fruit to deque
        2. bfs 
        - turn fresh fruit (1) to rotten fruit (2)
        3. iterate thru grid to check for fresh fruit
        - return -1 if there still r, else return level-1 (minutes)
        - floor level-1 to 0

        """

        # add rotten fruit to deque
        visited = set()
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
        
        # bfs - turn 1s to 2s
        level = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = 2

                # enqueue valid (fresh fruit) neighbors
                dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for dr, dc in dirs:
                    # out of bounds, visited, not a 1
                    if (r+dr == len(grid) or c+dc == len(grid[r]) or
                        min(r+dr, c+dc) < 0 or (r+dr, c+dc) in visited
                        or grid[r+dr][c+dc] != 1):
                        continue
                    
                    q.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))

            level += 1
        
        # if fresh fruit remaining after bfs, return -1
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return -1

        return max(0, level-1)


