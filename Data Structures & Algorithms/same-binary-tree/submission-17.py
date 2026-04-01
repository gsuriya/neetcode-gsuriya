# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):
            # both null - reached bottom at same time
            if not p and not q:
                return True

            # one null and not the other
            if not p and q or not q and p:
                return False

            # check equality of vals
            if p.val != q.val:
                return False

            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)

            # return and bubble up False, assume True until proven False
            return left and right

        return dfs(p, q)

