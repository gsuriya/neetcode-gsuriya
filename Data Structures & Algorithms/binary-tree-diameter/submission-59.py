# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """

        diameter of each node is left_height + right_height

        """

        max_diameter = float('-inf')

        def dfs(root):
            nonlocal max_diameter

            if not root:
                return 0

            left_height = dfs(root.left)
            right_height = dfs(root.right)
            
            max_diameter = max(max_diameter, left_height + right_height)


            return 1 + max(left_height, right_height)
        
        dfs(root)
        return max_diameter 