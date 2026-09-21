class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.n = len(board)   #Nr of rows
        self.m = len(board[0]) #Nr of cols
        self.ans = False

        starts = []

        # Scan the board to find all starting points
        for r in range(self.n):
            for c in range(self.m):
                if board[r][c] == word[0]:
                    starts.append((r, c))

        if not starts:
            return False
        
        for (r, c) in starts:
            seen = set()
            seen.add((r,c))
            self.backtrack(r, c, 1, word, seen, board)
        return self.ans
        
    def backtrack(self, r, c, i, word, seen, board):
        if i == len(word):
            self.ans = True
            return 
        for dr, dc in [(0,1), (1, 0), (-1, 0), (0, -1)]:
            if 0 <= r+dr < self.n and 0 <= c+dc < self.m and (r+dr, c+dc) not in seen and board[r+dr][c+dc] == word[i]:
                seen.add((r+dr, c+dc))
                self.backtrack(r+dr, c+dc, i+1, word, seen, board)
                seen.remove((r+dr, c+dc))
            

        


        