# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """

        for every node:
            - height(Lsub) - height(Rsub) within [-1, 1] 
        
        """

        def dfs(root):
            if not root: 
                # balanced, height
                return (True, 0)
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            # curr node balanced if:
            # - curr bf within range
            # - left/right subtrees r balanced
            curr_balanced = (-1 <= left[1]-right[1] <= 1) and left[0] and right[0] 

            # balanced, height
            return (curr_balanced, 1 + max(left[1], right[1]))
        

        return dfs(root)[0]



