# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0


        def dfs(root): # finds max_depth from a node
            nonlocal max_diameter

            if not root:
                return 0
            
            left = dfs(root.left) # = 0
            right = dfs(root.right) # = 3

            current_diameter = left + right
            max_diameter = max(current_diameter, max_diameter)

            return 1 + max(left, right)
        
        dfs(root)
        return max_diameter
