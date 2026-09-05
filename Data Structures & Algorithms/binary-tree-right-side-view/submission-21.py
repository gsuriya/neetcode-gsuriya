# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """

        enqueue right nodes first
        first one u pop is rightmost node

        """

        if not root:
            return []

        res = []
        q = deque([root])
        level = 0

        while q:
            for i in range(len(q)):
                curr = q.popleft()

                if i == 0:
                    res.append(curr.val)

                # enqueue neighbors
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
            
            level += 1
        
        return res
