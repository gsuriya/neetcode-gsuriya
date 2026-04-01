# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def bfs(root):
            if not root:
                return []

            right_side_nodes = []

            queue = deque([root])

            while queue:
                length = len(queue)
                for i in range(length):
                    curr = queue.popleft()

                    # if last node in queue popped, append to right_side_nodes
                    if i == length-1:
                        right_side_nodes.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)   

            return right_side_nodes 

        return bfs(root)

        