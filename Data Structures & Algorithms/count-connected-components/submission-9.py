class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """

        iterate thru n nodes
        - if node not in visited
        --> new component count++ and dfs on it to visit all


        """

        # create adj_list
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        # marks entire component as visited
        visited = set() 
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            # dfs on neighbors
            for nei in adj_list[node]:
                dfs(nei)

        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
        return count

        