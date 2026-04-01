# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        iterative BFS - basically j return # levels
        """
        if not root:
            return 0

        queue = deque([root])
        levels = 0

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                
                # enqueue children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels += 1
        
        return levels



