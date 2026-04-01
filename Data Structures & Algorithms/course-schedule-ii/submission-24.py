class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """

        build adj_list
        dfs start on every node

        as you bubble up, process nodes and add to res
        - if cycle at any point, return True --> return -1 right away before returning res

        """

        # build graph
        adj_list = defaultdict(list) # node --> [neighbors]
        for src, dst in prerequisites:
            adj_list[src].append(dst)
            _ = adj_list[dst]

        # populates res arr AND finds if cycle
        visited = set() # global for all dfs's
        visiting = set() # will be empty after a dfs
        def dfs(node):
            if node in visiting: # cycle found
                return True
            if node in visited:
                return False
            
            visited.add(node)
            visiting.add(node)

            # dfs on neighbors
            for nei in adj_list[node]:
                if dfs(nei): # cycle found --> bubble up True
                    return True
            
            visiting.remove(node)
            res.append(node)
        
        # dfs on every node - populate res arr
        res = []
        for node in range(numCourses):
            if dfs(node): # if any of them has a cycle return [] before returning res
                return []
        return res
            
        
