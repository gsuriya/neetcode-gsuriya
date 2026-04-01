# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """

        curr node diameter is max path

        return up max(left, right) to above root

        """
        max_path = float('-inf') # -5

        def dfs(root):
            nonlocal max_path

            if not root:
                return 0
            
            # throw away left or right if negative
            left = max(0, dfs(root.left)) # -5
            right = max(0, dfs(root.right)) # 0

            max_path = max(max_path, root.val + left + right)

            # return greater of left/right path
            return max(root.val+left, root.val+right)

        dfs(root)
        return max_path









