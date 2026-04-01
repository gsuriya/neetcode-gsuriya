# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        
        equivalent:
        - exact same structure
        - same values

        """

        def dfs(p, q):
            # reached bottom at diff times
            if (not p and q) or (not q and p):
                return False

            # reached bottom at same time
            if not p and not q:
                return True

            # diff values
            if p.val != q.val:
                return False

            
            left_same = dfs(p.left, q.left)
            right_same = dfs(p.right, q.right)

            return left_same and right_same

        return dfs(p, q)




