class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """

        for each u, v in edges
        - check if nodes u, v r alr connected --> edge to remove
        - if not, add to adj_list

        if there are multiple edges to be removed, removed[-1] should represent  the one that appears the most to the right in the initial edges list

        """
        # empty adjacency list to dfs thru
        adj_list = defaultdict(list)
        
        # checks if two nodes are connected in the adjacency list alr
        visited = set()
        def dfs(node, target):
            if node == target:
                return True
            if node in visited:
                return False
            
            visited.add(node)

            for nei in adj_list[node]:
                if dfs(nei, target):
                    return True
            
            visited.remove(node)
            
            return False

        # for each edge, check if alr connected or not
        removed = []
        for u, v in edges:
            if dfs(u, v): # connected
                removed.append([u, v])
            else: # ~connected
                adj_list[u].append(v)
                adj_list[v].append(u)

        return removed[-1]

