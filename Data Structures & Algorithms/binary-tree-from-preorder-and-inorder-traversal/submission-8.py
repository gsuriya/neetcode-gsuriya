# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        NODES OF GIVEN SUBTREE ARE GROUPED CONTIGUOUSLY

        """

        def dfs(preorder, inorder):
            if len(preorder) == 0:
                return
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            

            root = TreeNode(preorder[0])

            # find where preorder[0] is in inorder
            mid = inorder.index(preorder[0])

            # determine subarrays
            in_left = inorder[:mid]
            in_right = inorder[mid+1:]

            pre_left = preorder[1:1+len(in_left)]
            pre_right = preorder[1+len(in_left):]

            # pass in subarrays
            root.left = dfs(pre_left, in_left)
            root.right = dfs(pre_right, in_right)

            return root
        
        return dfs(preorder, inorder)
