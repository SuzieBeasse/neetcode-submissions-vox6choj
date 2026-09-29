class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) #nr of rows
        n = len(matrix[0]) #nr of cols

        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        
        # Binary search to find the row on which target is
        r = -1
        if target >= matrix[m-1][0]:
            r = m-1
        else:
            up = 0
            down = m-1

            while up < down:
                mid = (up + down) // 2
                if matrix[mid][0]== target or matrix[mid][n-1]==target:
                    return True
                elif matrix[mid][0] < target and matrix[mid][n-1] > target:
                    r = mid
                    break
                elif target < matrix[mid][0]:
                    down = mid -1
                else:
                    up = mid + 1
            
            if r == -1:
                r = down
        
        # Binary search to find if the target is in that row
        left = 0
        right = n-1

        while left < right:
            mid = (left + right)//2
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] > target:
                right = mid -1
            else:
                left = mid + 1
        
        return matrix[r][left] == target
        
        