class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """

        iterate thru n nodes:
        - if node not alr visited --> new component found (count += 1)
        - dfs and mark entire component as visited

        """

        # adj_list (graph to dfs thru) 
        # UNDIRECTED GRAPH
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        # marks entire connected component as visited to not recount it
        visited = set()
        def dfs(node): 
            if node in visited:
                return
            
            visited.add(node)

            for nei in adj_list[node]:
                dfs(nei)
            
            return

        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node) # dfs from node to mark entire component as visited
        return count


            