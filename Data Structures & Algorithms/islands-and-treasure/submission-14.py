class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        multi-source bfs starting from the treasure chests (0's)

        1. find coords of all 0s (by iterating)
        2. put 0s in bfs q, start it
        - popleft()
        - process: grid[r][c] == level
        - append children
           - out of bounds, visited, is a -1
        """

        q = deque()
        visited = set()
        level = 0

        # append all 0's
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        # start multi-source bfs
        while q:
            for _ in range(len(q)):
                # popleft
                r, c = q.popleft()

                # process
                grid[r][c] = level

                # append children
                neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
                for dr, dc in neighbors:
                    # out of bounds, visited, is a -1
                    if (r+dr == len(grid) or c+dc == len(grid[r]) or
                        min(r+dr, c+dc) < 0 or (r+dr, c+dc) in visited or
                        grid[r+dr][c+dc] == -1):
                        continue
                    q.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))

            level += 1

        return None









            