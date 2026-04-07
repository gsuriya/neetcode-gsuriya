class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """

        return # of islands

        iterate through:
        - if u hit a 1, then destroy it so u never hit it again
        - increment count

        """
        # destroy all 1s from here
        visited = set()
        def dfs(r, c):
            # out of bounds, in visited, not a 1
            if (r == len(grid) or c == len(grid[r]) 
                or min(r, c) < 0 or (r, c) in visited or
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
                    dfs(r, c) # destroys island so never see it again

        return count








        