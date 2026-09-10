class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """

        as you pop back, append to path

        cycle detection while u dfs
        - if cycle --> bubble up True and return []

        """

        # create adj_list (graph to iterate thru)
        adj_list = defaultdict(list)
        for src, dst in prerequisites:
            adj_list[src].append(dst)
            _ = adj_list[dst]
        # nodes w/ no connections auto mapped to [] b/c of defaultdict
        
        visited = set()
        visiting = set()
        path = []
        def dfs(node): # cycle detection + populates path as u backtrack
            if node in visiting:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            visiting.add(node)

            for nei in adj_list[node]:
                if dfs(nei):
                    return True # cycle found

            visiting.remove(node)
            path.append(node)

            return False # no cycle here
        
        # dfs on all nodes, if cycle return [] else path
        for node in range(numCourses):
            if dfs(node):
                return []

        return path

