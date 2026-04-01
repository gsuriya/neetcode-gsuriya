class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        "good" means increasing as you go down
        preorder pass down max_val
        - if node > max_val --> node is good

        1. mark nodes as good or not while passing down
        2. recurse back up, collecting count of good nodes
        """

        def dfs(root, max_val):
            if not root:
                return 0

            good_node = 1 if root.val >= max_val else 0
            max_val = max(max_val, root.val)

            left = dfs(root.left, max_val)
            right = dfs(root.right, max_val)

            return good_node + left + right

        return dfs(root, float('-inf'))


