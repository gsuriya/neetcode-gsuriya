class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        

        1. add all 2s (rotten fruit) to queue
        - and count # of fresh fruit


        2. multi-source bfs from 2s 

        while q:
            popleft()
            
            process: 
            - grid[r][c] == 2 (rotten)
            - if fresh == 0:
                return level

            append children
            - out of bounds, visited, is a 0 (only visit 1s, alr start @ 2s so visited)

        3. return -1 if fresh fruit still exist
        - if fresh: return -1

        """

        # step 1
        q = deque([])
        visited = set()
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        # step 2
        level = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                # process
                if grid[r][c] == 1:
                    fresh -= 1
                grid[r][c] = 2
                
                if fresh == 0:
                    return level
                
                # append children
                neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
                for dr, dc in neighbors:
                    # out of bounds, visited, is a 0
                    if (r+dr == len(grid) or c+dc == len(grid[r]) or
                        min(r+dr, c+dc) < 0 or (r+dr, c+dc) in visited or
                        grid[r+dr][c+dc] == 0):
                        continue
                    q.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))
            
            level += 1
        
        return -1


        