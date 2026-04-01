# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """

        recurse down

        1. if left/right subtree negative, dont bother including in sum
        2. include root.val in sum and return curr max_sum

        bubble up max_sum

        """
        max_sum = float('-inf')

        def dfs(root):
            nonlocal max_sum

            if not root:
                return 0
            
            # max_sum on left and right
            left = dfs(root.left)
            right = dfs(root.right)

            # calculate curr node max_sum, don't add negative left/right sums
            left, right = max(left, 0), max(right, 0)
            max_sum = max(max_sum, root.val + left + right)

            return root.val + max(left, right)
            
        dfs(root)
        return max_sum



