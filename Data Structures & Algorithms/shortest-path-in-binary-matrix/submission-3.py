class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        bfs - start @ level = 1

            popleft
            append children
            - out of bounds, visited, is a 1

        """

        q = deque([(0,0)])
        visited = set()
        visited.add((0,0))
        level = 1

        if grid[0][0] == 1:
            return -1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r == len(grid)-1 and c == len(grid[r])-1:
                    return level

                neighbors = [(0,1),(1,0),(-1,0),(0,-1),
                             (1,1),(-1,-1),(1,-1),(-1,1)]
                for dr, dc in neighbors:
                    if (r+dr == len(grid) or c+dc == len(grid[r]) or
                        min(r+dr, c+dc) < 0 or (r+dr,c+dc) in visited or
                        grid[r+dr][c+dc] == 1):
                        continue
                    q.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))

            level += 1

        return -1