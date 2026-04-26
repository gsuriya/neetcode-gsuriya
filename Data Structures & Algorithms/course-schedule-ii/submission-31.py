class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """

        if cycle --> can't take courses so return []

        else --> return topological sort

        """

        # create adj_list
        adj_list = {} # node --> [list of neighbors]
        for src, dst in prerequisites:
            if src not in adj_list:
                adj_list[src] = []
            if dst not in adj_list:
                adj_list[dst] = []
            adj_list[src].append(dst)
        # add rest of nodes NOT in edge list
        for course in range(numCourses):
            if course not in adj_list: # wasn't in edge list
                adj_list[course] = []

        # w/ cycle detection and topological sort
        visited = set()
        visiting = set()
        path = []
        def dfs(node):
            if node in visiting: # cycle detected
                return True
            if node in visited:
                return False
            
            visited.add(node)
            visiting.add(node)

            # dfs on neighbors
            for nei in adj_list[node]:
                if dfs(nei): # bubble up cycle detection
                    return True
            
            visiting.remove(node)
            path.append(node)
            
            return False # no cycle found

        # dfs on every node
        for course in range(numCourses):
            if dfs(course): # if cycle detected
                return []
        
        return path



        




