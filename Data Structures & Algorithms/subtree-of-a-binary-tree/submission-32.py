# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return False
            
            if root.val == subRoot.val and self.same_tree(root, subRoot):
                return True

            left = dfs(root.left)
            right = dfs(root.right)

            return left or right
        
        return dfs(root)

    def same_tree(self, p, q):
        # reached bottom at same time
        if not p and not q:
            return True
        
        # reached bottom at diff times
        if not p and q or not q and p:
            return False
        
        left = self.same_tree(p.left, q.left)
        right = self.same_tree(p.right, q.right)

        if p.val != q.val:
            return False
        
        return left and right

