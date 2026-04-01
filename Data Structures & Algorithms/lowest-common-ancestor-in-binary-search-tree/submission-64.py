# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """

        LCA is where split happens

        use "search" structure
        """

        def search(root):
            # search left
            if p.val < root.val and q.val < root.val:
                return search(root.left)
            # search right
            elif p.val > root.val and q.val > root.val:
                return search(root.right)
            # found
            else:
                return root

        return search(root)




