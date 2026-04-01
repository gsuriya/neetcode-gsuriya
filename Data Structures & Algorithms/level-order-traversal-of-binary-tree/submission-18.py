from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def bfs(root):
            nonlocal res

            if not root:
                return []
            
            q = deque([root])
            level = 0

            while q:
                level_arr = []
                for _ in range(len(q)):
                    curr = q.popleft()
                    level_arr.append(curr.val)

                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                    
                res.append(level_arr)
                level += 1

        bfs(root)
        return res











