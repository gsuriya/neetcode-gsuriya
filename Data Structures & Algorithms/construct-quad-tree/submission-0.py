"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        # divide and conquer on 2D grid, keep track of current n
        def dfs(n, r, c):
            # check if all same
            same = True
            for i in range(r, r+n):
                for j in range(c, c+n):
                    if grid[i][j] != grid[r][c]:
                        same = False 
            if same:
                root = Node(True if grid[r][c] == 1 else False, True)
            
            # else recurse, divide and conquer grid
            else:
                root = Node(True, False)
                root.topLeft = dfs(n//2, r, c)
                root.topRight = dfs(n//2, r, c+n//2)
                root.bottomLeft = dfs(n//2, r+n//2, c)
                root.bottomRight = dfs(n//2, r+n//2, c+n//2)
            
            return root

        return dfs(len(grid), 0, 0)



