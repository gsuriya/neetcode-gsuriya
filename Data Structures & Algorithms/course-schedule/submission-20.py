class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        
        1. construct adj list from prereqs edge list
        2. dfs that returns # courses completed
        - for cycles (visited set) bubble up -inf completed
        3. dfs on every node (full graph coverage for disconnected segments)
        - if completed = numCourses --> return True else False

        """

        # {int course : [int prereq, int prereq, int prereq, etc.]}
        adj_list = defaultdict(list)
        for src, dst in prerequisites:
            adj_list[src].append(dst)
            _ = adj_list[dst]

        # returns # of courses completed
        memoized = set() # nodes already had courses counted
        def dfs(node, visited):
            # base cases - visited, no prereqs
            if node in memoized:
                return 0
            if node in visited:
                return float('-inf')
            if not adj_list[node]:
                memoized.add(node)
                return 1
            
            visited.add(node)

            completed = 0            
            for neighbor in adj_list[node]:
                completed += dfs(neighbor, visited)

            
            memoized.add(node)
            
            return 1 + completed

        # start dfs from every node
        total_courses_completed = 0
        for i in range(numCourses):
            if i not in memoized: # makes it O(N) not O(N^2) cus ur doing dfs from every node
                total_courses_completed += dfs(i, set())

        return True if total_courses_completed == numCourses else False
            


        
