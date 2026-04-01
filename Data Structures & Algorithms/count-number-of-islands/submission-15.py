class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        """

        iterate through the array
        - if you find a 1
            - find REST of the island (dfs), change 1's to 0's
        - island_count += 1

        """

        # changes 1's to 0's for this island
        visited = set()
        def dfs(r, c):
            # out of bounds, visited
            if (min(r, c) < 0 or r == len(grid) or c == len(grid[r]) or 
            (r, c) in visited or grid[r][c] == "0"):
                return
            
            visited.add((r, c))

            grid[r][c] = "0" # change 1 to a 0

            # search in all directions now
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)

    
        island_count = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    # find rest of island, change 1's to 0's
                    dfs(r, c)
                    island_count += 1
        
        return island_count