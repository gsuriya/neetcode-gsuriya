class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """

        1. run a multi-source bfs starting from the rotten fruit
        - rotten fruit (2) spread to fresh fruit (1), avoid empty spaces (0)

        2. check if there are any fresh fruit
        - if there are, return -1
        - else return level

        """

        # add all rotten fruit as sources to q initialy
        q = deque()
        visited = set()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2: # rotten
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        if not fresh:
            return 0
        
        # start bfs
        level = 0
        while q:
            for _ in range(len(q)): # so level increments properly
                r, c = q.popleft()

                grid[r][c] = 2 # fresh --> rotten

                # append children - check if valid before appending to q
                neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for dr, dc in neighbors:
                    # out of bounds, visited, not a 1 (only fresh fruit)
                    if (r+dr == len(grid) or c+dc == len(grid[r]) or 
                        min(r+dr, c+dc) < 0 or (r+dr, c+dc) in visited or
                        grid[r+dr][c+dc] != 1):
                        continue
                    q.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))

            level += 1

        # check if any fresh fruit left, return -1 if there are else level
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return -1

        return level-1





