class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        def dfs(r, c):
            # out of bounds, visited, != 1
            if (r == len(grid) or c == len(grid[r]) or min(r, c) < 0 or 
                (r, c) in visited or grid[r][c] != "1"):
                return
            
            visited.add((r, c))
            grid[r][c] = "0"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    res += 1 # count it
                    dfs(r, c) # destroy island
        
        return res