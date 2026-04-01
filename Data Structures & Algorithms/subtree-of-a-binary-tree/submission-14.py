# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """

        for every node, check that its a subroot
        assume False until proven True

        """
        if not root:
            return False

        same = self.dfs(root, subRoot)
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        # if curr node same, or left or right node same bubble that True up
        return same or left or right


    # checks that its a same tree - assume True until proven False
    def dfs(self, p, q):
        # reached bottom @ diff times
        if (not p and q) or (not q and p):
            return False
        
        # reached bottom @ same time
        if not p and not q:
            return True
        
        # diff values
        if p.val != q.val:
            return False

        left = self.dfs(p.left, q.left)
        right = self.dfs(p.right, q.right)

        return left and right


