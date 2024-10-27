class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        nums = matrix

        # Create a DP table with the same dimensions as the matrix
        dp = [[0] * cols for _ in range(rows)]

        tot = 0

        for ind in range(rows):
            for j in range(cols):
                if nums[ind][j] == 1:
                    if ind == 0 or j == 0:
                        dp[ind][j] = 1
                    
                    else:
                        dp[ind][j] = min(dp[ind][j-1], dp[ind-1][j-1], dp[ind-1][j]) + 1
                    

                    tot += dp[ind][j]
        
        return tot