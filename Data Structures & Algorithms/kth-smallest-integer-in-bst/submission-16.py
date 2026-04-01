# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # do it iteratively instead of recursively

        res = []

        stack = []
        curr = root

        while curr or stack:
            # append left children
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # once curr reaches null on the left side, pop back up and PROCESS
            curr = stack.pop()
            res.append(curr.val)

            # go to the right and keep going left in next iteration
            curr = curr.right

        return res[k-1]
            

