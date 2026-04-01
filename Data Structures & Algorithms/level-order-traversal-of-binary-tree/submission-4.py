from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bst(root):
            if not root:
                return []
            queue = deque([root])

            level_map = defaultdict(list)
            level = 0
            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    level_map[level].append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                level += 1

            return list(level_map.values())
        
        return bst(root)