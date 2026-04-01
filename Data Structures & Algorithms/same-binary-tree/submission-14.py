# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:    

        def dfs(p, q):
            # reached bottom at same time
            if not p and not q:
                return True
            
            # one is null other isnt
            if not p and q or not q and p:
                return False
            
            # values aren't equal
            if p and q and p.val != q.val:
                return False

            # recursive calls - assume True, one False makes return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)
            

        return dfs(p, q) 