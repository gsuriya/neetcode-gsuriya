# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """

        make use of the fact that its a BST

        1. they split
        2. ancestor is also descendent

        """

        def dfs(root):
            if ((p.val <= root.val <= q.val) or 
                (q.val <= root.val <= p.val)):
                return root
            elif p.val < root.val and q.val < root.val:
                return dfs(root.left)
            elif p.val > root.val and q.val > root.val:
                return dfs(root.right)

        return dfs(root)







