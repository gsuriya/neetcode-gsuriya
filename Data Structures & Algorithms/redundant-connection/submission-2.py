class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """

        for each edge
        - check if u,v alr connected
        - if yes --> add to removed else add to graph

        return correct edge from removed list

        """

        # checks if u and v are connected alr
        def dfs(node, target, visited):
            if node == target:
                return True
            if node in visited:
                return False
            
            visited.add(node)

            # dfs on neighbors
            for nei in adj_list[node]:
                if dfs(nei, target, visited):
                    return True
            return False

        removed = []
        adj_list = defaultdict(list)
        for u, v in edges:
            # alr connected
            if dfs(u, v, set()):
                removed.append([u, v])
            # NOT alr connected
            else:
                adj_list[u].append(v)
                adj_list[v].append(u)
        
        for i in range(len(edges)-1, -1, -1):
            if edges[i] in removed:
                return edges[i]
        





        