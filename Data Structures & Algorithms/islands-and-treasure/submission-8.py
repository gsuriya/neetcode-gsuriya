class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        O(nigesh) time

        multi-source bfs
        - initial sources are the GATES
        - each square will have distance to CLOSEST gate b/c bfs will mark squares earlier than others and mark as visited so later bfs's dont remark it
        """

        def bfs():
            queue = deque()
            visited = set()
            length = 0

            # populate queue with source gates
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] == 0: # this is a gate
                        queue.append((r, c))

            # run bfs from each gate, update each square with current level
            while queue:
                for _ in range(len(queue)): # of nodes in current level
                    r, c = queue.popleft()
                    grid[r][c] = length

                    # enqueue the children
                    deltas = [[0,1], [0,-1], [1,0], [-1,0]]
                    for dr, dc in deltas:
                        curr_r, curr_c = r+dr, c+dc
                        # in bounds, visited, -1, 0
                        if (min(curr_r, curr_c) < 0 or curr_r == len(grid) or curr_c == len(grid[curr_r]) or
                           (curr_r, curr_c) in visited or grid[curr_r][curr_c] == -1 or grid[curr_r][curr_c] == 0):
                           continue
                        queue.append((curr_r, curr_c))
                        visited.add((curr_r, curr_c))

                length += 1

        bfs()
