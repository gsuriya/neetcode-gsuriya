# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        1. prorder traversal through root tree
         - once root.val = subroot.val --> check that rest of nodes are equal

        """

        subtree = False

        # assume False at start
        def dfs(root, subRoot):
            nonlocal subtree

            if not root:
                return False

            # Preorder traversal on root tree
            if root.val == subRoot.val:
                # check if other nodes are the same
                subtree = self.isSameTree(root, subRoot)
                if subtree:
                    return


            left = dfs(root.left, subRoot)
            right = dfs(root.right, subRoot)
        
        dfs(root, subRoot)
        return subtree

    
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

            

