from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid) #nr of rows
        n = len(grid[0]) #nr of cols

        queue = deque([])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        dis = 0

        while queue:
            level = len(queue)
            dis += 1
            for _ in range(level):
                r, c = queue.popleft()

                for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if 0 <= r+dr < m and 0 <= c+dc < n and grid[r+dr][c+dc] > dis:
                        grid[r+dr][c+dc] = dis
                        queue.append((r+dr, c+dc))
        
        
        