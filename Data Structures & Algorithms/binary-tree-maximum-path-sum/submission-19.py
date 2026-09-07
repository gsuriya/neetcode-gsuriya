# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        
        use global var always for max/min

        1. floor to 0 to cut off left/right sums
        2. sum everything, update max_sum
        3. return max of left and right branch

        """
    
        max_sum = float('-inf')
        def dfs(root):
            nonlocal max_sum

            if not root:
                return 0
            
            # floor
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            # sum and update
            max_sum = max(max_sum, root.val + left + right)

            # return highest sum branch
            return max(root.val + left, root.val + right)

        dfs(root)
        return max_sum

