class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        equal or lower
        return cells [r, c] such that they can go to both

        1. dfs from pacific, pacific visited set
        2. dfs from atlantic, atlantic visited set
        3. return intersection(pacific, atlantic)

            0 1 2 3 4
        0  [4,2,7,3,4],
        1  [7,4,6,4,7],
        2  [6,3,5,3,6]
        """

        # reverse water spread
        def dfs(r, c, prev_height, visited):
            # out of bounds, visited, not reverse
            if (r == len(heights) or c == len(heights[r]) or 
                min(r, c) < 0 or (r, c) in visited or
                heights[r][c] < prev_height):
                return
            
            visited.add((r, c))

            dfs(r+1, c, heights[r][c], visited)
            dfs(r-1, c, heights[r][c], visited)
            dfs(r, c+1, heights[r][c], visited)
            dfs(r, c-1, heights[r][c], visited)

        # dfs all the pacific cells & atlantic cells
        pacific = set()
        atlantic = set()
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                if r == 0 or c == 0:
                    # pacific
                    dfs(r, c, float('-inf'), pacific)
                if r == len(heights)-1 or c == len(heights[r])-1:
                    # atlantic
                    dfs(r, c, float('-inf'), atlantic)

        # return intersection
        res = []
        for coord in pacific:
            if coord in atlantic:
                res.append([coord[0], coord[1]])
        return res





