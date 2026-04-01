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

        def dfs(root, cumulative_max):
            if not root:
                return 0

            cumulative_max = max(cumulative_max, root.val)

            good_node = 1 if root.val >= cumulative_max else 0

            left = dfs(root.left, cumulative_max) # num good nodes on left
            right = dfs(root.right, cumulative_max) # num good nodes on right

            return good_node + left + right
        
        return dfs(root, float('-inf'))