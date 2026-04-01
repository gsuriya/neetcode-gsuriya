# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        base case: if len(preorder) == 1: return node

        1. create node with root = preorder[0]
        2. pass rest of nodes to dfs(left) & dfs(right)
        - use inorder to PARTITION preorder AND inorder into left & right

        preorder = 3 9 20 15 7 
        inorder =  9 3 15 20 7

        """

        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None

            root = TreeNode(preorder[0])

            # find where preorder[0] is in inorder
            mid = inorder.index(preorder[0])

            in_left = inorder[:mid]
            in_right = inorder[mid+1:]

            pre_left = preorder[1:1+len(in_left)]
            pre_right = preorder[1+len(in_left):]

            # passing in modified inorder, preorder arrays
            root.left = dfs(pre_left, in_left)
            root.right = dfs(pre_right, in_right)

            return root
        
        return dfs(preorder, inorder)
