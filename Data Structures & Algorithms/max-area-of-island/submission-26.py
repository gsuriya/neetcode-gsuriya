class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """

        1. iterate until find a 1
        - calculate max area, dynamically update max
        - blow up island so never encounter it again

        """

        # returns area (count of 1s) of island
        visited = set()
        def dfs(r, c):
            # out of bounds, visited, is a 0
            if (r == len(grid) or c == len(grid[r]) or min(r, c) < 0 or
                (r, c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r, c))

            count = 1 + dfs(r+1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1)
            
            return count


        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area

