class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = defaultdict(list)
        for src, dst in prerequisites:
            adj_list[src].append(dst)
            _ = adj_list[dst]
        
        for node in range(numCourses):
            _ = adj_list[node]
        
        """
        total_completed = 1
        path = [0]

        1 --> 0

        2

        """

        # returns number of courses completed starting at this node
        # -- need visited set so dont double count courses
        visited = set()
        visiting = set()
        def dfs(node):
            if node in visiting: 
                return float('-inf') # cycle detected
            
            if node in visited:
                return 0
                # case 1: node already counted don't recount
                # case 2: curr node gets a 0 returned, idk to count curr node or not
            if not adj_list[node]: # no prereqs, can take
                visited.add(node)
                path.append(node)
                return 1
            
            visited.add(node)
            visiting.add(node)

            completed = 0
            for nei in adj_list[node]:
                completed += dfs(nei)
            
            visiting.remove(node)
            path.append(node)

            return 1 + completed
            
        
        # run dfs on every node in graph, generate completed
        path = []
        total_completed = 0
        for node in range(numCourses):
            total_completed += dfs(node)

        if total_completed == numCourses:
            return path
        else:
            return []



