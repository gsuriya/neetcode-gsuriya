# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # telling us specifically a BST --> make use of values
        vals = []

        def inOrder(root):
            if not root:
                return

            inOrder(root.left)
            vals.append(root.val)
            inOrder(root.right)
        
        inOrder(root)
        return vals[k-1]
            