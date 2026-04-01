# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """

        all nodes in left subtree less
        all nodes in right subtree more

        pass domain: (start w/ [-inf, inf])
        - go right --> right bound = root
        - go left --> left bound = root

        assume True unless proven False (bubble up False)
        """

        def dfs(root, left_bound, right_bound):
            if not root:
                return True
            
            if not (left_bound < root.val < right_bound):
                return False

            # boolean for whether left/right subtrees r valid BSTs
            left = dfs(root.left, left_bound, root.val)
            right = dfs(root.right, root.val, right_bound)

            return left and right

        
        return dfs(root, float('-inf'), float('inf'))

