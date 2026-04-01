# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        max_diameter = 0

        def max_depth(root):
            nonlocal max_diameter

            if not root:
                return 0

            left = max_depth(root.left)
            right = max_depth(root.right)

            # dia @ each node = max_depth on the left + max_depth on the right
            curr_diameter = left + right
            max_diameter = max(max_diameter, curr_diameter)

            return 1 + max(left, right)
        
        max_depth(root)
        return max_diameter