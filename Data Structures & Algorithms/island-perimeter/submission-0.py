class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """

        return number of invalid sides for each node
        island --> so start dfs from first 1 we see

        """

        visited = set()
        def dfs(r, c):
            # visited
            if (r, c) in visited:
                return 0
            # out of bounds or water defines perimeter unit
            if (r == len(grid) or c == len(grid[r]) or min(r, c) < 0 or
               grid[r][c] == 0):
                return 1
            
            visited.add((r, c))
            
            count = (
                dfs(r+1, c) +
                dfs(r-1, c) +
                dfs(r, c+1) +
                dfs(r, c-1)
            )

            return count

        # find 1 --> start dfs
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return dfs(r, c)


        

