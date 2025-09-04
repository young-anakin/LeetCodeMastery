class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # space is going to be a 2D array

        matrix = [[0 for _ in range((n))] for _ in range(m) ]
        print(matrix)

        def inbound(i, j):
            return i >= 0 and j >= 0 and i < m and j < n
        
        matrix[0][0] = 1
        # matrix[0][1] = 1
        # matrix[1][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                # print(i, j, inbound(i, j-1), inbound(i-1, j))
                up, down = 0, 0
                if inbound(i-1, j):
                    up = matrix[i-1][j]
                if inbound(i, j-1):
                    down = matrix[i][j-1]
                matrix[i][j] = up + down
        
        print(matrix)
        return matrix[m-1][n-1]

                
