class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """

        don't need visiting and visited, js visited cus dfs'ing
        from only one node to check len(visited)

        1. connected - can reach ALL nodes len(visited) = n
        2. no cycles

        """

        # create adj_list
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        # dfs from one node, check for cycles in UNDIRECTED graph
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return True # cycle detected

            visited.add(node)

            # dfs on every nei except parent
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if dfs(nei, node): 
                    return True
            
            return False

        if dfs(0, -1):
            return False # cycle found --> not valid tree
        
        if len(visited) != n: # not all nodes found from dfs --> not connected
            return False
        
        return True
        

            


