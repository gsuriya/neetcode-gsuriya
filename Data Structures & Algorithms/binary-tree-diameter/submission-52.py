# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """

        bubble up max_diameter and dynamically update at each node

        """

        def dfs(root):
            # return val: height, max_dia so far
            if not root:
                return (0, 0)
            
            left = dfs(root.left) # (0,0)
            right = dfs(root.right) # (3,3)

            curr_diameter = left[0] + right[0] # 2 + 1 = 3

            max_diameter = max(curr_diameter, left[1], right[1])

            return (1 + max(left[0], right[0]), max_diameter)
            

        return dfs(root)[1]