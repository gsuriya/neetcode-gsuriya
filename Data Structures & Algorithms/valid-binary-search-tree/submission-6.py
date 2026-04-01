# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
                2
            1       3

            pass bounds preorder
            L: min = float('-inf')  max = root.val
            R: min = root.val       max = float('inf')
    
        """

        def dfs(root, min_, max_):
            if not root:
                return True
            
            # left and right valid

            left = dfs(root.left, min_, root.val)
            right = dfs(root.right, root.val, max_)

            # determine if curr node valid
            curr = left and right and min_ < root.val < max_

            return curr
        
        return dfs(root, float('-inf'), float('inf'))

