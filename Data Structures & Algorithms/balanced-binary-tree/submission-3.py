# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(root): # finds depth for node
            nonlocal balanced

            if not balanced:
                return 0

            if not root:
                return 0 
            
            left = dfs(root.left) # = 1
            right = dfs(root.right) # = 2

            # use left and right depth to calculate balance factor
            if not -1 <= (left - right) <= 1:
                balanced = False
                return 0

            return 1 + max(left, right)

        dfs(root)
        return balanced
        


