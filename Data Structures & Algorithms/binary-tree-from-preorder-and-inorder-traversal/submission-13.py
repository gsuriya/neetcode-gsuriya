# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """

        preorder: root, left, right

        inorder:  left, root, right

        1. preorder to find root, build
        2. inorder to find left and right subtrees
        --> pass recursively until left and right subtrees []

        """

        def dfs(preorder, inorder):
            if not preorder and not inorder:
                return None

            root = TreeNode(preorder[0])

            # inorder find length of left subtree
            i = 0
            while inorder[i] != preorder[0]:
                i += 1
            
            # pass left and right subtrees recursively
            root.left = dfs(preorder[1:1+i], inorder[:i])
            root.right = dfs(preorder[i+1:], inorder[i+1:])

            return root
        
        return dfs(preorder, inorder)




