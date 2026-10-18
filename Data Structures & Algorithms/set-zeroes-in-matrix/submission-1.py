class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix) #nr of rows
        n = len(matrix[0]) #nr of columns
        first_row = 1
        first_col = 1

        for r in range(m):
            if matrix[r][0] == 0:
                first_col = 0

        for c in range(n):
            if matrix[0][c] == 0:
                first_row = 0


        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if first_row == 0:
            for c in range(n):
                matrix[0][c] = 0
 
        if first_col == 0:
            for r in range(m):
                matrix[r][0] = 0

        return
                



        
        