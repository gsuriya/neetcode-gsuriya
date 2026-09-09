class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """

        1. dfs: simulate reverse water flow
        - visited sets to track nodes that pacific and atlantic reached
        3. return intersection of those sets

        """

        # simulates reverse waterflow and populates the visited set
        def dfs(r, c, visited, prev): # curr > prev
            # out of bounds, visited, need to be moving upwards 
            if (r == len(heights) or c == len(heights[r]) or min(r, c) < 0
                or (r, c) in visited or heights[r][c] < prev):
                return
            
            visited.add((r, c))

            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        # dfs from all of the edges and populate visited sets
        pacific, atlantic = set(), set()
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                # pacific
                if r == 0 or c == 0:
                    dfs(r, c, pacific, float('-inf'))
                # atlantic
                if r == len(heights)-1 or c == len(heights[r])-1:
                    dfs(r, c, atlantic, float('-inf'))

        # return intersection of those sets
        res = []
        for coord in pacific:
            if coord in atlantic:
                res.append(coord)
        return res



