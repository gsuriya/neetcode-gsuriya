# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # tuple solution

        def dfs(root):
            if not root:
                return (0, 0) # (max_dia, height)
            
            left = dfs(root.left)
            right = dfs(root.right)

            max_diameter = max(left[0], right[0], left[1]+right[1])
            height = 1 + max(left[1], right[1])

            return (max_diameter, height)
        
        return dfs(root)[0]


