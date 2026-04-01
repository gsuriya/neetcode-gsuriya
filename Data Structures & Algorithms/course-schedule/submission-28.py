class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacency list
        adj_list = defaultdict(list)
        for src, dst in prerequisites:
            adj_list[src].append(dst)
            _ = adj_list[dst]


        """

        two possible methods
        1. completed == numCourses
        2. graph cycle detection (CHOSEN)


        1 --> 2   4 ---> 5
        ^     |
        |     |
        ------3

        """

        # dfs cycle detection
        visiting = set() # same dfs call collapses on itself
        visited = set() # so other dfs calls don't recheck nodes

        def dfs(node):
            if node in visiting: # loop detected
                return True # want True to bubble up
            if node in visited: # dont recheck alr processed node
                return False
            
            visited.add(node)
            visiting.add(node)

            cycle = False
            for nei in adj_list[node]:
                if dfs(nei):
                    cycle = True
            visiting.remove(node)

            return cycle

        # dfs from every starting node
        for node in range(numCourses):
            if dfs(node):
                return False # cycle found
        
        return True # no cycle found








        
