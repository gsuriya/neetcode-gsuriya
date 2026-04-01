class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """

        1. adj_map using prereqs list
        2. dfs on ALL nodes (adj_map could be disconnect)
        - node state 1: visited in current iterative dfs
        - node state 2: memoized and counted alr

        if loop in graph --> return []

        1 <-- 4
        |     |
        0 --> 2 --> 3

        base case edge list = []:
            path.append(node)
            return path

        base case visited hit:
            have False in tuple, return up dont care ab path appending

        path.append(node)
        return path
        """

        adj_map = defaultdict(list)
        for src, dst in prerequisites:
            adj_map[src].append(dst)
            _ = adj_map[dst]
        
        memoized = set()
        path = []
        def dfs(node, visited):
            # base cases - visited, no prereqs
            if node in visited:
                # theres a loop
                return False
            if node in memoized:
                # already processed
                return True
            
            memoized.add(node)
            visited.add(node)

            for neighbor in adj_map[node]:
                if not dfs(neighbor, visited):
                    return False

            visited.remove(node)
           
            path.append(node)

            return True
        
        for i in range(numCourses):
            if i not in memoized:
                if not dfs(i, set()):
                    return []
        
        return path
