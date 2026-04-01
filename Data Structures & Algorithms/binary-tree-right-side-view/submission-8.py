# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """

        bfs but only print the last value in each level

        2, 3
        """

        def bfs(root):
            res = []

            if not root:
                return []

            q = deque([root])
            level = 0

            while q:
                q_length = len(q)
                for i in range(len(q)):
                    curr = q.popleft()
                    
                    # append last elem in level
                    if i == q_length-1:
                        res.append(curr.val)

                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)

                level += 1
            
            return res
        
        return bfs(root)