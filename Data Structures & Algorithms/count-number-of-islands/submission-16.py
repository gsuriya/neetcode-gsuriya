class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """

        iterate through array
        
        if a 1 is found, turn all of it to 0s
        - the next 1 found means new island

        """


        # delete 1s starting from here
        visited = set()
        def dfs(r, c):
            # out of bounds, visited, is a 0
            if (r == len(grid) or c == len(grid[r]) or
                min(r, c) < 0 or (r, c) in visited or
                grid[r][c] == "0"):
                return
            
            visited.add((r, c))
            grid[r][c] = "0" # switch "1" to "0"

            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)


        island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    # dfs to delete 1s starting from here
                    dfs(r, c)
                    island_count += 1
        
        return island_count


