# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        BFS - return number of levels
        """

        def bfs(root):
            if not root:
                return 0

            queue = deque([root])

            level = 0
            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                level +=1
            
            return level
        
        return bfs(root)


