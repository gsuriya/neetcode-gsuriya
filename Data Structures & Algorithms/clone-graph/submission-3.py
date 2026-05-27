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

        undirected --> two-way connections

        1. create nodes
        2. create pointers

        """
        if not node:
            return

        visited = {} # visited --> cloned nodes

        def dfs(node):
            if node in visited:
                return visited[node] # return cloned counterpart

            # clone node
            clone = Node(node.val)
            visited[node] = clone

            # add cloned neighbors to neighbors list
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        return dfs(node)









