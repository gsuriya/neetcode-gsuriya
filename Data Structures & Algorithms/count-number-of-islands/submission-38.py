class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """

        iterate
        - hit an island 

        """

        # destroys the island (turns to 0s)
        visited = set()
        def dfs(r, c):
            # out of bounds, visited
            if (r == len(grid) or c == len(grid[r]) or 
                min(r, c) < 0 or (r, c) in visited or 
                grid[r][c] != "1"):
                return
            
            visited.add((r, c))
            grid[r][c] = "0"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        
        return count


