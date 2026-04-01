# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # return last val at each level

        def bfs(root):
            if not root:
                return []

            queue = deque([root])
            res = [] # last vals at each level

            while queue:
                lenQ = len(queue)
                for i in range(lenQ):
                    curr = queue.popleft()
                    if i == lenQ-1:
                        res.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            
            return res
        
        return bfs(root)