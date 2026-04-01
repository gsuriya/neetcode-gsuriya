# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """

        specifically a binary SEARCH tree --> make use of that

        1. inorder traversal array
        2. return inorder[k-1]

        """
        res = []
        def inOrder(root):
            if not root:
                return None

            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return res[k-1]
            

