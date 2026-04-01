from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """

        return list of level order traversal; therefore, bfs

        """

        

        def bfs(root):
            res = []

            if not root:
                return []
            
            level = 0
            q = deque([root])

            while q:
                level_vals = []
                for _ in range(len(q)):
                    curr = q.popleft()
                    level_vals.append(curr.val)

                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                
                res.append(level_vals)
                level += 1
            
            return res
        
        return bfs(root)
       










