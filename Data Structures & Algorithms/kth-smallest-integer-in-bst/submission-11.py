# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """

        find kth value and then bubble it up

        """
        count = k

        def dfs(root):
            nonlocal count

            if not root:
                return None
            
            left = dfs(root.left)
            
            count -= 1
            if count == 0: # kth val found --> bubble it up
                return root.val

            right = dfs(root.right)

            return left if left else right
        
        return dfs(root)


