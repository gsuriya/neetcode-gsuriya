# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        """

        goal: rebuild the tree from these two traversals

       

        thoughts:
        - 1st elem of preorder is always root
        - Q: what are the ACTUAL immediate children for the root node?
        - A: elemns ahead of root in preorder r immediate children
        - EUREKA: think traversal lists as SUBTREES
        
        steps:
        RECURSIVE:
        1. build 1st elem of preorder as root
        2. index of root in inorder --> find split for left/right subtrees in preorder arr
        3. pass subarr left/right subtree for preorder & preorder


        preorder = [1,2,3,4] (root, left, right)
         - w/ j preorder, can't tell if root is left/right child
          
                     i
        inorder = [2,1,3,4] (left, root, right)
        - inorder helps determine if root is left/right child

        """

        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None

            # create root node
            root = TreeNode(preorder[0])

            # find split of left/right subtrees in preorder arr
            i = 0
            while i < len(inorder):
                if inorder[i] == preorder[0]:
                    break
                i += 1
            
            # pass in next dfs calls
            root.left = dfs(preorder[1:1+i], inorder[:i])
            root.right = dfs(preorder[1+i:], inorder[i+1:])

            return root

        return dfs(preorder, inorder)
 






