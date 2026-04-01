# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        write max_depth function
        use subcalculations of max_depth function to calculate boolean balanced

        once boolean balanced calculated for left/right subtree, 
        node balanced should be based on balanced for left/right as well
        """

        def dfs(root, balanced):
            if not root:
                return [0, True] # Null node has height of 0 and is balanced
            
            left = dfs(root.left, balanced)
            right = dfs(root.right, balanced)

            # calculate balance using left/right calculations
            # if the left or right subtrees are not balanced, whole tree isnt balanced
            if not left[1] or not right[1] or not -1 <= (left[0] - right[0]) <= 1:
                balanced = False

            # (height, balanced)
            return (1 + max(left[0], right[0]), balanced)
        
        return dfs(root, True)[1]

