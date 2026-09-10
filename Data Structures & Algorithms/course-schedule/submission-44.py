class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """

        if cycle in graph --> can't take all courses

        1. create adj_list from edge list
        2. cycle detection using visiting set

        """

        # create adj_list
        adj_list = defaultdict(list)
        for src, dst in prerequisites:
            adj_list[src].append(dst)
            _ = adj_list[dst]

        # dfs cycle detection using visiting set
        visited = set()
        visiting = set()
        def dfs(node):
            if node in visiting:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            visiting.add(node)

            # dfs on neighbors
            for nei in adj_list[node]:
                if dfs(nei):
                    return True
            
            visiting.remove(node)

            return False

        # dfs from every node cus disconnected graph
        for node in range(numCourses):
            if dfs(node):
                return False
        return True


