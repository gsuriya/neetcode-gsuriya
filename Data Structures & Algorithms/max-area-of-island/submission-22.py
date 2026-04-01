class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """

        iterate thru grid
        - grid[r][c] == 1 --> blow it up + return max_area
        - max_area = max(dfs(r,c), max_area)
        - return @ end


        """
        def dfs(r, c):
            # out of bounds, visited - handled by turning to 0
            if min(r, c) < 0 or r == len(grid) or c == len(grid[r]) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0 # marking as visited

            area = 1 + dfs(r+1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1)


            return area

        max_area = float('-inf')

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    max_area = max(dfs(r, c), max_area)
        
        if max_area == float('-inf'):
            return 0
        
        return max_area