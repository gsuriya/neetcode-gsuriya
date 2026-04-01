# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same_tree(p, q): # compare bottom up
            # reach bottom at diff times
            if (not p and q) or (not q and p):
                return False
            # reach bottom at same time
            if not p and not q:
                return True
            
            left = same_tree(p.left, q.left)
            right = same_tree(p.right, q.right)

            return left and right and p.val == q.val


        def dfs(root):
            if not root:
                return False

            left = dfs(root.left)
            right = dfs(root.right)

            exists = False
            if root.val == subRoot.val:
                exists = same_tree(root, subRoot)
            
            return left or right or exists
        
        return dfs(root)
    

        





