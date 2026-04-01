# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """

        calculate the balance factor (bf) of every node

        bf = heightL - heightR

        if any node's bf not in [-1, 1], then tree is not balanced

        """

        def dfs(root):
            if not root:         # (height, balanced)
                return (0, True) # assume empty tree is balanced
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            height = 1 + max(left[0], right[0])
            balanced = left[1] and right[1] and -1 <= left[0]-right[0] <= 1

            return (height, balanced)
        
        return dfs(root)[1]







