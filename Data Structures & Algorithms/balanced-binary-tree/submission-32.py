# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # calculate the balance factor of every node
        # bf = height(left) - height(right)
        # if bf not in [-1, 1] return False, else True

        """
        what do i need to calculate the bf at a node?

        1. height of left and height of right

        """

        def dfs(root):
            if not root:
                return [0, True] # Null nodes have height of 0 and are balanced

            left = dfs(root.left)
            right = dfs(root.right)

            balanced = True
            bf = left[0] - right[0]
            if not -1 <= bf <= 1 or not left[1] or not right[1]:
                balanced = False 

            if not balanced:
                return [0, False]

            # (height, balanced)
            return (1 + max(left[0], right[0]), balanced)

        return dfs(root)[1]