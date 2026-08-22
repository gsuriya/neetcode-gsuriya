class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """

        iterate thru
        - island hit --> count area and update max, mark as visited
        - wont recount island area cus in visited

        """

        # counts area of island
        visited = set()
        def dfs(r, c):
            # out of bounds, visited, is a 0
            if (r == len(grid) or c == len(grid[r]) or min(r, c) < 0 or
                (r, c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r, c))

            return 1 + (
                dfs(r+1, c) + 
                dfs(r-1, c) +
                dfs(r, c+1) +
                dfs(r, c-1)
            )
            
        
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))

        return max_area


