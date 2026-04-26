class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """

        1. dfs from pacific and atlantic cells
        -  add to pacific, atlantic sets
        2. return intersection of sets
        - intersection represents coords that can get to BOTH oceans

        curr_val > prev

        """

        # dfs from oceans
        def dfs(r, c, visited, prev):
            # out of bounds, visited, going up
            if (r == len(heights) or c == len(heights[r]) or min(r, c) < 0 or
                (r, c) in visited or heights[r][c] < prev):
                return
            
            visited.add((r, c))

            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        # dfs from pacific and atlantic borders
        pacific, atlantic = set(), set()
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                if r == 0 or c == 0: # pacific
                    dfs(r, c, pacific, float('-inf'))
                if r == len(heights)-1 or c == len(heights[r])-1: # atlantic
                    dfs(r, c, atlantic, float('-inf'))
        
        # return intersection
        res = []
        for coord in pacific:
            if coord in atlantic:
                res.append([coord[0], coord[1]])
        return res










