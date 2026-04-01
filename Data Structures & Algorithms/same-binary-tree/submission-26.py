# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        the recursion tree is aligned with the structural overlap of the p and q trees
        """

        def dfs(p, q):
            # reach the bottom at diff times
            if (p and not q) or (q and not p):
                return False
            # reach bottom at same time
            if not p and not q:
                return True
            
            # values are different
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)

            return left and right and p.val == q.val
        
        return dfs(p, q)




        
