# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """

        dfs through both trees at same time

        """

        def dfs(p, q):
            if not p and not q: # reach bottom same time
                return True
            if (not p and q) or (not q and p): # reach bottom at diff time
                return False
            
            if p.val != q.val:
                return False

            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)

            
            
            return left and right
        
        return dfs(p, q)
            
            