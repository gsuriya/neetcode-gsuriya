class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """

        iterate thru
        - island hit --> dynamically update max area, mark as visited
        - return max_area

        """

        visited = set()
        def dfs(r, c):
            # out of bounds, visited
            if (r == len(grid) or c == len(grid[r]) or min(r, c) < 0 or
                (r, c) in visited or grid[r][c] != 1):
                return 0
            
            visited.add((r, c))

            count = 1 + (
                dfs(r+1, c) + 
                dfs(r-1, c) +
                dfs(r, c+1) +
                dfs(r, c-1)
            )

            return count

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area

