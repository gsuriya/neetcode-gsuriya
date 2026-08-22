"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """

        clone node, attach neighbors

        """

        visited = {} # visited --> cloned

        def dfs(node):
            if node in visited:
                return visited[node]

            # clone node, establish hashmap connection
            clone = Node(node.val)
            visited[node] = clone

            # attach neighbors
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            
            return clone
        
        if not node:
            return None

        return dfs(node)






