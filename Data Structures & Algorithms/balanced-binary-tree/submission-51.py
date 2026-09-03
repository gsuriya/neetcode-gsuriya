# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """

        tuple return

        """

        def dfs(root):
            if not root:
                return (0, True) # (height, balanced)
            
            left = dfs(root.left)
            right = dfs(root.right)

            height = 1 + max(left[0], right[0])
            balanced = -1 <= left[0]-right[0] <= 1 and left[1] and right[1]

            return (height, balanced)

        return dfs(root)[1]




