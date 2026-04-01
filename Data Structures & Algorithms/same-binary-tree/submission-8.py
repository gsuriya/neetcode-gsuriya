# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:    
        same_tree = True

        def dfs(p, q):
            nonlocal same_tree
            if not same_tree:
                return

            # base cases
            if not p and not q:
                return
            
            # if one null and one valid
            if (p and not q) or (q and not p):
                same_tree = False
            if p and q and p.val != q.val:
                same_tree = False

            if same_tree:
                dfs(p.left, q.left)
                dfs(p.right, q.right)

        dfs(p, q)
        return same_tree        