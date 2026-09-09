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

        dfs normally
        - checking back like how u would in normal dfs also forms 
          connections now w/ the base case

        hashmap to connect old to new nodes

        """

        visited = {None: None} # old --> new

        def dfs(node):
            if not node or node in visited:
                return visited[node] # cus u want undirected
            
            # create clone and add connection
            clone = Node(node.val)
            visited[node] = clone

            # dfs on neighbors
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei)) # like root.left = dfs()
            
            return clone
        
        return dfs(node)





