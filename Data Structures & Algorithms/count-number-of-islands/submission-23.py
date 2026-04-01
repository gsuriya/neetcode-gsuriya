class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        encounter an island:
        - increment island_count
        - blow up island

        """

        visited = set()
        def dfs(r, c): # turn all 1s to 0s
            # out of bounds, visited, only go to 1s
            if (r == len(grid) or c == len(grid[r]) or min(r, c) < 0 or
                (r, c) in visited or grid[r][c] != "1"):
                return
            
            visited.add((r, c))

            grid[r][c] = "0"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    island_count += 1
                    dfs(r, c)
        return island_count






