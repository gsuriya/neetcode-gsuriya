# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root: # (curr_sum, max_sum)
                return (float('-inf'), float('-inf'))
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            # discard negative sums from left/right
            left_sum = 0 if left[0] < 0 else left[0]
            right_sum = 0 if right[0] < 0 else right[0]

            curr_sum = root.val + left_sum + right_sum
            max_sum = max(curr_sum, left[1], right[1])

                      # return only L/R path
            return (root.val + max(left_sum, right_sum), max_sum)
        
        return dfs(root)[1]

