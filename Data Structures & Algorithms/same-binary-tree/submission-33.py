# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """

        dfs at the same time on both trees

        """

        def dfs(p, q):
            if not p and not q:
                return True
            if not p and q or not q and p:
                return False
            
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)

            if p.val != q.val:
                return False
            
            return left and right
        
        return dfs(p, q)


