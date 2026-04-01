class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        iterate through ALL

        if you hit a 1, annihilate the island (set 1s to 0s)
         - increment island_count
        
        if you hit any more 1s, you know this is a NEW island so annihilate and do increment island_count again

        """


        # dfs to annihilate island
        visited = set()
        def dfs(r, c):
            # base cases - out of bounds, visited, "0"
            if min(r, c) < 0 or r == len(grid) or c == len(grid[r]) or (r, c) in visited or grid[r][c] == "0":
                return

            # only on 1s now
            grid[r][c] = "0" # get rid 1

            visited.add((r,c))
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            visited.remove((r,c))

        island_count = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1": # island found
                    dfs(r, c) # annihilate it
                    island_count += 1
        
        return island_count


