# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        
        # u already know what this recursive function does
        # so just say what the recursive variables store in english
        # left stores the max depth of the left subtree
        # right stores the max depth of the right subtree

        def dfs(root):
            nonlocal max_diameter

            if root == None:
                return 0

            leftDFS = dfs(root.left)
            rightDFS = dfs(root.right)

            # find max diameter at EACH node
            max_diameter = max(max_diameter, leftDFS + rightDFS)

            # finds max depth at EACH node
            return 1 + max(leftDFS, rightDFS)

        dfs(root)
        return max_diameter