class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """

        water flows from HIGH --> LOW

        return list of r,c 


        1. create set of (r, c) that can be reached from atlantic
        2. create set of (r, c) that can be reached from pacific
        3. intersection of these two sets
        
        
        """

        atlantic = set()
        pacific = set()

        def dfs(r, c, prev, ocean):
            # out of bounds, visited, water level (low --> high)
            if (r == len(heights) or c == len(heights[r]) or
                min(r, c) < 0 or (r, c) in ocean or
                prev > heights[r][c]):
                return
            
            ocean.add((r, c))

            dfs(r+1, c, heights[r][c], ocean)
            dfs(r, c+1, heights[r][c], ocean)
            dfs(r-1, c, heights[r][c], ocean)
            dfs(r, c-1, heights[r][c], ocean)


        # start dfs from edges
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                # pacific
                if r == 0 or c == 0:
                    dfs(r, c, heights[r][c], pacific)
                # atlantic
                if r == len(heights)-1 or c == len(heights[0])-1:
                    dfs(r, c, heights[r][c], atlantic)

        # return intersection set
        intersection = []
        for coord in atlantic:
            if coord in pacific:
                intersection.append([coord[0], coord[1]])
        
        return intersection

















        

        