class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """

        1. multi-source bfs from rotten fruit
        2. if no fresh fruit --> return level else return -1
        - iterate thru grid to see if fresh fruit remaining

        """

        # add rotten fruit as initial sources
        visited = set()
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    visited.add((r, c))
                    q.append((r, c))
        
        # start multi-source bfs
        level = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = 2

                # enqueue neighbors
                dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for dr, dc in dirs:
                    # out of bounds, visited, != 1
                    if (r+dr == len(grid) or c+dc == len(grid[r]) or
                        min(r+dr, c+dc) < 0 or (r+dr, c+dc) in visited or
                        grid[r+dr][c+dc] != 1):
                        continue
                    
                    visited.add((r+dr, c+dc))
                    q.append((r+dr, c+dc))
            
            level += 1
        

        # check if fresh fruit remaining
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return -1
        
        return max(0, level-1)




