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
        - helps determine root

        inorder: left, root, right
        - determine sizes of left and right subtrees w/ root
        
        
                            1 2 3 4
                            2 1 3 4

                    2                   3 4
                    2                   3 4
                                             4

        """
        # pass left/right subtrees for preorder and inorder lists
        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None
        
            root = TreeNode(preorder[0])
            i = 0
            while i < len(inorder) and inorder[i] != preorder[0]:
                i += 1

            root.left = dfs(preorder[1:1+i], inorder[:i])
            root.right = dfs(preorder[1+i:], inorder[i+1:])

            return root
        
        return dfs(preorder, inorder)








