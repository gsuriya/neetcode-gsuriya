class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        1 - fresh
        2 - rotten

        goal: return # levels to make ALL fruit rotten
         - or return -1 if not possible

        1. multi-source bfs starting from rotten fruit
        2. iterate through grid to check for any fresh fruit
           - return -1 if fresh fruit
           - return levels if not
        """

        def bfs():
            queue = deque()
            visited = set()
            levels = 0

            # add rotten fruits as initial sources
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] == 2:
                        queue.append((r, c))
                        visited.add((r, c))
            
            while queue:
                for _ in range(len(queue)): # snapshot of nodes in current level
                    r, c = queue.popleft()
                    grid[r][c] = 2 # make current fruit rotten

                    # enqueue children
                    deltas = [[1,0], [-1,0], [0,1], [0,-1]]
                    for rd, cd in deltas:
                        curr_r, curr_c = r+rd, c+cd
                        #  out of bounds, visited, has to be a fruit
                        if (min(curr_r, curr_c) < 0 or curr_r == len(grid) or curr_c == len(grid[curr_r]) or
                           (curr_r, curr_c) in visited or grid[curr_r][curr_c] != 1):
                           continue

                        queue.append((curr_r, curr_c))
                        visited.add((curr_r, curr_c))

                levels += 1
            
            return levels
        
        levels = bfs()

        # if fresh fruit exists, return -1, else return levels
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return -1
        return 0 if levels-1 < 0 else levels-1