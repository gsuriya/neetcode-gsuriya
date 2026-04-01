# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """

        inorder traversal
        get to the kth value, bubble it up

        """
        count = k
        res = 0

        def dfs(root):
            nonlocal count, res

            if not root:
                return
            
            dfs(root.left)

            count -= 1
            if count == 0:
                res = root.val
                
            dfs(root.right)
        
        dfs(root)
        return res
            

