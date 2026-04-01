# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """

        preorder pass down the max value
        if curr.val > max_val --> this is a good node

        bubble up # of good nodes

        """

        def dfs(root, max_val):
            if not root:
                return 0
            
            good_node = 1 if root.val >= max_val else 0
            max_val = max(max_val, root.val)

            left = dfs(root.left, max_val)
            right = dfs(root.right, max_val)

            return good_node + left + right
        

        return dfs(root, float('-inf'))