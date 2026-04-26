class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """

        arbitrary graph cycle detection


        1. make adj_list from edge list
        2. dfs from every node 
        - visiting and visited set

        """
        
        # make adj_list from edges
        adj_list = {} # node --> [list of neighbors]
        for src, dst in prerequisites:
            if src not in adj_list:
                adj_list[src] = []
            if dst not in adj_list:
                adj_list[dst] = []
            adj_list[src].append(dst)

        visited = set()
        visiting = set() # return True if cycle detected
        def dfs(node):
            # visiting - cycle detected
            if node in visiting:
                return True
            # visited
            if node in visited:
                return False
            
            visited.add(node)
            visiting.add(node)

            # dfs neighbors
            for nei in adj_list[node]:
                if dfs(nei):
                    return True # bubble up cycle found

            visiting.remove(node)
            
            return False

        # dfs from every node - cycle detection
        for course in range(numCourses):
            if course not in adj_list:
                adj_list[course] = []

            if dfs(course):
                return False
        
        return True




