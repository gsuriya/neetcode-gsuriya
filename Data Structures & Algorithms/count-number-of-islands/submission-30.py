class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """

        return # of islands

        if u hit a 1, then delete an island
        - any other 1 will mean a new island

        dfs --> deletes all the island (1s)

        """

        visited = set()
        def dfs(r, c):
            # out of bounds, not valid
            if (r == len(grid) or c == len(grid[r]) or min(r, c) < 0 or
                (r, c) in visited or grid[r][c] != "1"):
                return
            
            visited.add((r, c))
            grid[r][c] = "0"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    island_count += 1
                    dfs(r, c) # delete island
        
        return island_count

