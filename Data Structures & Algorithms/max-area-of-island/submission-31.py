class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """

        find an island --> return the max area of it
        - its marked as visited so you never go never recount the island

        """

        visited = set()
        def dfs(r, c):
            # out of bounds, in visited, is not a 1
            if (r == len(grid) or c == len(grid[r]) or min(r, c) < 0 or 
                (r, c) in visited or grid[r][c] != 1):
                return 0
            
            visited.add((r, c))
            
            count = (
                dfs(r+1, c) +
                dfs(r-1, c) +
                dfs(r, c+1) +
                dfs(r, c-1)
            )

            return 1 + count
        
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    # dfs, return area of island
                    max_area = max(max_area, dfs(r, c))
        return max_area


