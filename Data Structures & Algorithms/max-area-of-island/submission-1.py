class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid) #nr of rows
        m = len(grid[0]) #nr of columns
        max_area = 0
        
        def dfs(r: int, c: int) -> int:
            ans = 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= r+dr < n and 0<= c+dc < m and grid[r+dr][c+dc] == 1:
                    grid[r+dr][c+dc] = 0
                    ans += dfs(r+dr, c+dc)
            return ans
        

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    a = dfs(r, c)
                    max_area = max(max_area, a)
                    
        
        return max_area

    