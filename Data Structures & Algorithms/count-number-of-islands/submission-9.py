class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        if hit a 1, blow up that island, increment island count
        if another 1, you know another island, increment island count
        """

        # deletes all the 1s given start point
        visited = set()
        def dfs(r, c):
            # base cases - out of bounds, visited, "0"
            if (min(r, c) < 0 or r == len(grid) or c == len(grid[r]) or
               grid[r][c] == "0" or (r, c) in visited):
               return
            
            visited.add((r, c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

       
        
        island_count = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r,c) not in visited and grid[r][c] == "1": # island found
                    dfs(r, c) # blow it up
                    island_count += 1
        
        return island_count
