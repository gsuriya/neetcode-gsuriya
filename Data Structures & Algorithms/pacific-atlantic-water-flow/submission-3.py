class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """

        dfs from each edge of square

        1. dfs from pacific ocean - build squares that can reach pac
        2. dfs from atlantic ocean - build squares that can reach atl
        3. return intersection of pac and atl set

        """
        pac_visited = set()
        atl_visited = set()

        def dfs(r, c, visited, prev_height):
            # base cases - out of bounds, visited, lower height
            if (min(r, c) < 0 or r == len(heights) or c == len(heights[0]) or
               (r, c) in visited or prev_height > heights[r][c]):
               return

            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        # call dfs on heights edge squares
        # top (pac) and bottom (atl)
        for r in range(len(heights)):
            if r == 0: # pacific
                for c in range(len(heights[r])):
                    dfs(r, c, pac_visited, heights[r][c])
            if r == len(heights)-1: # atlantic
                for c in range(len(heights[r])):
                    dfs(r, c, atl_visited, heights[r][c])
        
        # left (pac) and right (atl)
        for c in range(len(heights[0])):
            if c == 0: # pacific
                for r in range(len(heights)):
                    dfs(r, c, pac_visited, heights[r][c])
            if c == len(heights[0])-1: # atlantic
                for r in range(len(heights)):
                    dfs(r, c, atl_visited, heights[r][c])

        return list(pac_visited.intersection(atl_visited))

        

        