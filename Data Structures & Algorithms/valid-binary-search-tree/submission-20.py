# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """

        pass domain down into each node

                -inf, inf
                    1
        -inf, 1           1, inf
            0                3
                      1, 3
                        2



        if root isn't within domain, bubble up false

        """

        def dfs(root, low, high):
            if not root: # empty tree is valid
                return True
            
            if not low < root.val < high:
                return False

            left = dfs(root.left, low, root.val)
            right = dfs(root.right, root.val, high)

            return left and right

        return dfs(root, float('-inf'), float('inf'))




