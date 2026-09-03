# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """

        global flag
        left and right heights at each node can't differ by 1

        """

        is_balanced = True
    
        def dfs(root):
            nonlocal is_balanced

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if not -1 <= left-right <= 1:
                is_balanced = False

            return 1 + max(left, right)
        
        dfs(root)
        return is_balanced

