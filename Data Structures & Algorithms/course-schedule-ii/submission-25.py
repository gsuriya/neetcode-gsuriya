class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """

        if cycle --> return [] else return valid topological sort
        
        """

        # create adj_list
        adj_list = defaultdict(list)
        for src, dst in prerequisites:
            adj_list[src].append(dst)
            _ = adj_list[dst]

        # find cycle else populate topological sort (path)
        visited = set()
        visiting = set()
        def dfs(node, path):
            if node in visiting:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            visiting.add(node)

            for nei in adj_list[node]:
                if dfs(nei, path):
                    return True # bubble up True

            path.append(node)
            visiting.remove(node)
            return False

        # dfs on every course
        path = []
        for node in range(numCourses):
            if dfs(node, path):
                return []
        
        return path





