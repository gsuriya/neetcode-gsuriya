# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """

        can't assume its a binary SEARCH tree

        1. they split
        2. ancestor is also descendent

        """

        def dfs(root):
            if not root:
                return None
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                return root

            if root == p or root == q:
                return root
            
            if left: return left
            if right: return right

        return dfs(root)



