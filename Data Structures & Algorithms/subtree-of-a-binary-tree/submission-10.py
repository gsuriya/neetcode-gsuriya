# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # both null
        if not root and not subRoot:
            return True
        
        # root null subtree not
        if not root and subRoot:
            return False

        # only recurse if current node is equal
        if self.sameTree(root, subRoot):
            return True
        
        # assume False until proven True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def sameTree(self, p, q):
        # both reach bottom at same time
        if not p and not q:
            return True
        
        # one null and other isn't - possible edge case: null subtree of non-empty tree
        if (not p and q) or (not q and p):
            return False
        
        # check values
        if p.val != q.val:
            return False
        
        # bubble of recursive value
        left = self.sameTree(p.left, q.left)
        right = self.sameTree(p.right, q.right)

        # true until proven false --> use "and" to bubble up False
        return left and right

