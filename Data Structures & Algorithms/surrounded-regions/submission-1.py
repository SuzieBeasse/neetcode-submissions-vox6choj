class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        m = len(grid) #nr of rows
        n = len(grid[0]) #nr of cols

        self.resist = set()

        def dfs( r, c):
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= r+dr < m and 0 <= c+dc < n and grid[r+dr][c+dc] == 'O' and (r+dr, c+dc) not in self.resist:
                    self.resist.add((r+dr, c+dc))
                    dfs(r+dr, c+dc)

        # Check the regions that are not surrounded by looking at the edges
        for r in range(m):
            for c in [0, n-1]:
                if grid[r][c] == "O" and (r, c) not in self.resist:
                    self.resist.add((r, c))
                    dfs(r, c)
        
        for r in [0, m-1]:
            for c in range(n):
                if grid[r][c] == "O" and (r, c) not in self.resist:
                    self.resist.add((r, c))
                    dfs(r, c)
        
        # Go through the grid and change the zeros that are not in resist
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "O" and (r, c) not in self.resist:
                    grid[r][c] = 'X'

    
        

        