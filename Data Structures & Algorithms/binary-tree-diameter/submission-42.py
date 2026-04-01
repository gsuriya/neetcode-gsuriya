# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        diameter at each node is height(root.left) + height(root.right)

        calculate the height but also have the max_diameter being bubbled up
        """

        def dfs(root):
            if not root:
                return (0, 0) # null node: height=0, diameter=0
            
            left = dfs(root.left)
            right = dfs(root.right)

            # diameter calculation
            curr_diameter = left[0] + right[0]
            # bubble up max diameter - compare curr_diameter against L and R returns
            diameter = max(curr_diameter, left[1], right[1])

            # (height, diameter)
            return (1 + max(left[0], right[0]), diameter)

        return dfs(root)[1]