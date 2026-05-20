class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        build adjacency list

        for every node
        - dfs --> marks everything as done
        - on next iteration if node is NOT in visited --> new connected component


        """
        # build adjacency list
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
        for node in range(n):
            if node not in adj_list:
                _ = adj_list[node]

        # mark all nodes as visited
        visited = set()
        def dfs(node):
            # visited
            if node in visited:
                return
            
            visited.add(node)

            # dfs on neighbors
            for nei in adj_list[node]:
                dfs(nei)

        # dfs on every node
        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
        return count





