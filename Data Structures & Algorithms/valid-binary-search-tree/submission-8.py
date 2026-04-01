# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """

                2
            (-inf, inf)
            1         3
        (-inf, 2)   (2, inf)
       3           2.5     4
      (-inf,1)   (2, 3)   (3, inf)
        

        domain of left child: (curr_min, root.val)
        domain of right child: (root.val, curr_max)
        """

        def dfs(root, min_, max_):
            if not root:
                return True
            
            # pass in min and max constraints into left and right
            # whether left and right are valid BSTs
            left = dfs(root.left, min_, root.val)
            right = dfs(root.right, root.val, max_)

            # curr node is valid BST or not
            curr_valid = left and right and min_ < root.val < max_

            return curr_valid

        return dfs(root, float('-inf'), float('inf'))