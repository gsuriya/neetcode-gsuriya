# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    1. understand normal post order return that is not base case from previous problems ive done
    2. understand its calculating CURRENT node and that left and right are INTEGERS so like setting good_node before that doesn't matter at all

    return res after L and R recursive calls makes SENSE
    b/c think of L and R calls as just returning base case
    and then you do return the res and it bubbles up

    """
    def goodNodes(self, root: TreeNode) -> int:

        # good node if > maxVal seen so far
        def dfs(root, maxVal):
            if not root:
                return 0

            good_node = 1 if root.val >= maxVal else 0
            maxVal = max(maxVal, root.val)
            left = dfs(root.left, maxVal)
            right = dfs(root.right, maxVal)

        
            return good_node + left + right
        
        return dfs(root, root.val)






