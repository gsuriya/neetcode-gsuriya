# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    """

    NULLs are stop signs
    --> any traversal works

    preorder chosen b/c EASIEST TO DESERIALIZE
    - preorder is NATURAL way to construct tree (create root and add children)

    """
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = []

        def dfs(root):
            if not root:
                preorder.append('NONE')
                return
            
            preorder.append(f'{root.val}')
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ','.join(preorder)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """

                           i
        preorder = [1, 2, None, None, 3, 4, None, None, 5, None, None]

                1
            2

        """
        preorder = data.split(',')
        i = 0

        def dfs():
            nonlocal i
            
            if i == len(preorder) or preorder[i] == 'NONE':
                i += 1
                return

            root = TreeNode(preorder[i])
            i += 1

            root.left = dfs()
            root.right = dfs()

            return root
        
        return dfs()











