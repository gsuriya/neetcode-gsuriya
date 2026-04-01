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

        YOU WANT A FALSE FROM THE LEFT AND RIGHT CALLS TO BUBBLE UP
        """

        def dfs(root): # checks height of each node and calculates bf
            if not root:
                return [0, True] # for null: height = 0, bf = 0 --> True
            
            left = dfs(root.left) # height of left node
            right = dfs(root.right) # height of right node

            # "and" --> assumes True even one False bubbles up
            balanced = None
            if left[1] and right[1] and -1 <= (left[0] - right[0]) <= 1:
                balanced = True
            else:
                balanced = False

            # return (height, balanced)
            return (1 + max(left[0], right[0]), balanced)


        return dfs(root)[1]



