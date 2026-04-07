class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """

        if cycle --> return False else True

        steps:
        1. construct adj_list from edge list 
        2. dfs on every node


        """

        # construct adj_list
        adj_list = defaultdict(list)
        for src, dst in prerequisites:
            adj_list[src].append(dst)
            _ = adj_list[dst]

        visited = set() # don't re-explore paths
        visiting = set() # loop detection
        def dfs(node):
            # loop detected
            if node in visiting:
                return True
            # in visited
            if node in visited:
                return False
            
            visited.add(node)
            visiting.add(node)

            # neighbors
            for nei in adj_list[node]:
                if dfs(nei): # bubble up True
                    return True
            
            visiting.remove(node)
            return False
        
        # dfs on every node, check for cycle
        for node in range(numCourses):
            if dfs(node):
                return False

        return True
        

        