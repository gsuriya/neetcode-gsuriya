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
        
        max_path = float('-inf')

        def dfs(root):
            nonlocal max_path

            if not root:
                return 0
            
            # throw away left or right if negative
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            max_path = max(max_path, root.val + left + right)

            # return greater of left or right paths
            return max(root.val+left, root.val+right)

        dfs(root)
        return max_path









