# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # return True if -1 <= (max_depth(left) - max_depth(right)) <= 1
        # else False
        balanced = True

        def max_depth(root):
            nonlocal balanced

            # if alr found, j exit out faster w/o recursing more
            if not balanced:
                return 0

            if not root:
                return 0

            left = max_depth(root.left)
            right = max_depth(root.right)

            if not -1 <= (left - right) <= 1:
                balanced = False
                

            return 1 + max(left, right)
        
        max_depth(root)
        return balanced



