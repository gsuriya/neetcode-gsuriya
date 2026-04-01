class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """

        return False if cycle else True if not

        1. build adjacency list
        2. start dfs on every node (visited set so O(N))
        - visiting set as well to detect cycle

        """

        # build adjacency list
        adj_list = defaultdict(list)
        for src, dst in prerequisites:
            adj_list[src].append(dst)
            _ = adj_list[dst]
        

        # dfs to find cycle - return True if cycle
        visiting = set() # detect cycles on same path
        def dfs(node):
            if node in visiting: # cycle found
                return True
            if node in visited: # alr explored this region
                return False
            
            visited.add(node)
            visiting.add(node)

            # dfs on neighbors - bubble up True
            for nei in adj_list[node]:
                if dfs(nei):
                    return True
                    
            visiting.remove(node)
            
            return False

        
        # start dfs on every node
        visited = set()
        for node in range(numCourses):
            if dfs(node): # found a cycle
                return False
        
        return True


