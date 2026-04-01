# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    # preorder serialization
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(root):
            if not root:
                res.append("N")
                return

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ",".join(res)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        
        # global i cus don't want to backtrack on string
        self.i = 0 # can also use normal i = 0 w/ nonlocal syntax

        def dfs():
            if data[self.i] == "N":
                self.i += 1
                return None
            
            root = TreeNode(data[self.i])
            
            self.i += 1
            root.left = dfs()
            root.right = dfs()

            return root 
            
        return dfs()











