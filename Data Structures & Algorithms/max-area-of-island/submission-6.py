class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        # return area of an island
        visited = set()
        def dfs(r, c):
            # base cases - out of bounds, visited, "0"
            if (min(r, c) < 0 or r == len(grid) or c == len(grid[r]) or
               (r, c) in visited or grid[r][c] == 0):
               return 0 
            
            visited.add((r, c))

            area = 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)        

            return area



        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    # mark this entire island, calculate area
                    area = dfs(r, c)
                    max_area = max(area, max_area)
        
        return max_area